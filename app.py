import streamlit as st 
import openai
import os, json
from dotenv import load_dotenv
from datetime import datetime
from questions import QUESTIONS

load_dotenv()

def initialize_session_state():
    if "messages" not in st.session_state:
        # Create a chat history for each question (each tab)
        st.session_state.messages = {i: [] for i in range(len(QUESTIONS))}
    if "current_tab" not in st.session_state:
        # We'll default to the first question (tab 0). (You can add code later to update this on tab switch.)
        st.session_state.current_tab = 0

def log_interaction(question_idx, user_input, assistant_response):
    """
    Log each interaction to a JSON file with timestamp
    """
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "question_number": question_idx,
        "question_title": QUESTIONS[question_idx]['question_title'],
        "user_input": user_input,
        "assistant_response": assistant_response
    }
    
    log_file = "interaction_log.jsonl"
    
    # # Read existing logs if file exists
    # try:
    #     with open(log_file, 'r') as f:
    #         logs = json.load(f)
    # except (FileNotFoundError, json.JSONDecodeError):
    #     logs = []
    
    # Append new log entry
    # logs.append(log_entry)
    
    # Write updated logs back to file
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry)+'\n')

def get_llm_response(message, question_idx, response_placeholder):
    client = openai.Client(
        base_url=os.environ["R1_URL"],
        api_key=os.environ["R1_API_KEY"]
    )
    system_message = f"""You are one of the best teacher in the world.
You ask a question to student.
If the student is able to answer then good, else you ask subsequent questions which help in getting to the answer.
You can praise the good things, tell about positives in answer, can provide some feedback (but not solution), and then ask subsequest question to arrive at answer.
Your goal is to help the student discover the solution on their own through a series of well-crafted questions.

Qualities of your voice and Tone: Calm, insightful voice of reason. Naturally enthusiastic.

Right now the question that you have posed is:

Problem Statement:
```
{QUESTIONS[question_idx]['question']}
```

Solution:
```
{QUESTIONS[question_idx]['solution']}
```

Below are example questions provided are just a starting point. Tailor your subsequent questions based on the student's current understanding and responses.
```
{QUESTIONS[question_idx]['example_problems']}
```

Ask only one question at a time, it could be a combination of above questions or you can think something new as per the requirement.
You can praise the good things, tell about positives in answer, can provide some feedback (but not solution), and then ask subsequest question to arrive at answer.
But do not provide the solution or answer.
Your goal is to help the student discover the solution on their own through a series of well-crafted questions.

Qualities of your voice and Tone: Calm, insightful voice of reason. Naturally enthusiastic.

Conversation So Far -
You: {QUESTIONS[question_idx]['question']}

"""
    for message in st.session_state.messages[question_idx]:
        if message["role"] == "user":
            system_message += f"Student: {message['content']}\n\n"
        elif message["role"] == "assistant":
            system_message += f"You: {message['content']}\n\n"
    
    system_message += "You: "
    print(system_message)
    full_response = ""
    # Create a streaming response
    stream = client.chat.completions.create(
        model='deepseek-r1',
        messages=[{"role": "system", "content": system_message}],
        stream=True
    )
    
    tmp_placeholder_values = ["...", "...", "...", "...",
                              "....", "....", "....", "....",
                              ".....", ".....", ".....", ".....",
                              "......", "......", "......", "......"]
    counter = 0
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            if '</think>' in full_response:
                # Update the placeholder with the accumulated response (with a blinking cursor)
                response_placeholder.markdown('</think>'.join(full_response.split('</think>')[1:]) + "▌")
            else:
                counter += 1
                response_placeholder.markdown(tmp_placeholder_values[counter % 16])
    
    # Final update without the cursor
    response_placeholder.markdown('</think>'.join(full_response.split('</think>')[1:]))
    return full_response

def main():
    st.set_page_config(page_title="Interactive Learning Platform", layout="wide")
    initialize_session_state()
    
    # CSS styling
    st.markdown("""
    <style>
    /* Hide default Streamlit menus */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display: none;}
    footer {visibility: hidden;}
    div.block-container {padding-top: 0rem;}
    header {height: 0 !important;}
    
    /* Header styling */
    .centered-content {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .image {
        height: 4rem;
        margin-right: 10px;
    }
    .text {
        font-size: 1.25rem;
        font-weight: bold;
        padding-top: 1rem;
        padding-left: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('''
    <div class="centered-content">
      <img src="https://static.wixstatic.com/media/fb00f0_6aa0505e4a9949fd8da8735e0ee54b1e~mv2.png/v1/fill/w_206,h_93,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/fb00f0_6aa0505e4a9949fd8da8735e0ee54b1e~mv2.png" alt="Your Image" class="image">
      <p style="font-size: 3rem">|</p>
      <p class="text">Interactive Learning Platform</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Select the active question via a sidebar radio button.
    # (This replaces st.tabs so that only the active question's content is displayed.)
    tab_names = [QUESTIONS[i]['question_title'] for i in range(len(QUESTIONS))]
    active_tab = st.sidebar.radio("", options=list(range(len(QUESTIONS))),
                                  format_func=lambda i: tab_names[i])
    st.session_state.current_tab = active_tab
    
    # Display the content for the active question
    question = QUESTIONS[active_tab]
    st.markdown(f"#### {question['question_title']}")
    st.markdown(question['question'])
    
    # Display chat history for the active question
    for message in st.session_state.messages[active_tab]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input inside the active tab container
    prompt = st.chat_input(f"Your thoughts on - {question['question_title']}")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        # Append the user's message to the active question’s chat history
        st.session_state.messages[active_tab].append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response = get_llm_response(prompt, active_tab, response_placeholder)
        st.session_state.messages[active_tab].append({"role": "assistant", "content": '</think>'.join(response.split('</think>')[1:])})

        log_interaction(active_tab, prompt, response)
        # Rerun so that the updated conversation is displayed
        st.rerun()

if __name__ == "__main__":
    main()
