# questions.py
QUESTIONS = [
    {'question': """Imagine there are a 100 people in line to board a plane that seats 100. The first person in line, Alice, realizes she lost her boarding pass, so when she boards she decides to take a random seat instead. Every person that boards the plane after her will either take their "proper" seat, or if that seat is taken, a random seat instead.

**Question:** What is the probability that the last person that boards will end up in their proper seat?""",
    'question_title': "Airplane Boarding Problem",
    'example_problems': """**Building Intuition**
1. If there are 2 passengers and 2 seats, what's the probability the last passenger gets their seat if the first picks randomly?
2. With 3 passengers, list all possible scenarios when Passenger 1 chooses randomly. How many result in Passenger 3 getting their seat?
3. For 3 passengers, what pattern do you notice between who takes Passenger 1's seat vs others?
4. In the 3-passenger case, what's special about when Passenger 1 picks either their own seat or the last seat?

**Pattern Recognition**
5. For 4 passengers, what happens if Passenger 1 chooses:
   a) Their own seat
   b) Passenger 4's seat
   c) Passenger 2's seat
   d) Passenger 3's seat
6. In scenario 5c, what problem does this create for Passenger 2?
7. In scenario 5d, what new sub-problem gets created?
8. For n passengers, what two critical seats determine the final outcome?

**Recursive Thinking**
9. How does the 3-passenger problem relate to the 2-passenger version?
10. If we have n passengers and the first picks seat k (1 < k < n), what smaller version of the problem gets created?
11. What's always true about the relationship between the first and last seats in these recursive cases?

**Probability Analysis**
12. In the 4-passenger case, calculate the probability:
    - Direct success (Passenger 1 picks seat 1)
    - Direct failure (Passenger 1 picks seat 4)
    - Recursive cases (Passenger 1 picks seats 2 or 3)
13. How does the probability distribute between success and failure in the recursive cases?
14. What mathematical pattern emerges from adding these probabilities?

**Generalization**
15. For n passengers, let P(n) be the probability the last passenger gets their seat. Write the recursive formula.
16. Through substitution, show that P(n) = P(n-1) = ... = P(2)
17. What's the fundamental reason the probability remains constant regardless of n?
18. Why doesn't the number of intermediate passengers affect the final probability?

**Formal Proof**
19. How can we use induction to prove P(n) = 1/2 for all n ≥ 2?
20. What's the base case for induction?
21. What's the inductive step?
22. How does the recursive nature of the problem support the induction hypothesis?

**Intuitive Explanation**
23. Imagine the first person's choice as starting a "chain reaction." Why does this chain ultimately only care about the first and last seats?
24. How does this problem relate to the concept of "absorbing states" in probability?
25. If you had to explain why the answer is 1/2 in one sentence, what symmetry argument would you use?

The learner should discover that:
- The probability always resolves to 50/50
- The key seats are always the first and last
- Intermediate choices create recursive subproblems that maintain the probability ratio
- The solution relies on symmetry and recursive probability preservation

This builds from concrete examples through pattern recognition to formal proof, developing both intuitive understanding and mathematical rigor.
""",
    'solution': """The probability that the last person boards their proper seat is **1/2** (50%). This counterintuitive result holds regardless of the number of passengers, as long as there are at least two people. Here's why:

### Key Reasoning
1. **First passenger's choice creates a chain reaction**:
   - Alice (first passenger) randomly selects either:
     - Her own seat (resolving the conflict immediately)
     - The last passenger's seat (dooming the last passenger)
     - A middle seat, transferring the problem to another passenger

2. **Recursive nature**:
   - When a displaced passenger (e.g., passenger k) enters, they face the same dilemma Alice did but with fewer remaining seats
   - This creates identical probabilistic conditions at each displacement stage

3. **Symmetry argument**:
   - The last seat available when final passenger boards must be either:
     - First passenger's original seat (seat 1)
     - Last passenger's assigned seat (seat 100)
   - These two outcomes are equally likely due to random selection symmetry

### Mathematical Proof
For _n_ passengers:
- Let _P(n)_ = probability last passenger gets their seat
- Base case: _P(2)_ = 1/2
- Recursive relation:  
  _P(n)_ = (1/n) + (n-2)/n × _P(n-1)_
- Solving this recurrence relation shows _P(n)_ = 1/2 for all _n_ ≥ 2

### Real-World Interpretation
- 50% chance Alice either indirectly fixes the seating chaos by ultimately occupying her own seat or the last passenger's seat
- All intermediate displacements cancel out probabilistically
- Formula works for any number of passengers ≥ 2
"""},

{
    'question': """An Egg breaks only if dropped from above a threshold floor, within a 100-story building. Every time you drop an egg, it is counted as an attempt. You are given 2 eggs to deduce the threshold floor, with a minimum number of attempts in the worst case!""",
    'question_title': "Egg Drop Problem",
    'example_problems': """**Building Intuition**

1. **Single Egg Baseline:**  
   *If you had only one egg, how would you determine the threshold floor in a 100‑story building?*  
   *(Hint: You’d have to start from the first floor and work upward one floor at a time.)*

2. **Cost with One Egg:**  
   *What is the worst-case number of drops needed when using only one egg?*

3. **Advantage of Two Eggs:**  
   *How does having a second egg potentially allow you to reduce the number of drops compared to the one‑egg scenario?*

4. **After a Break:**  
   *When the first egg breaks, what must be done with the second egg in order to find the exact threshold floor?*

**Initial (Naïve) Strategies**

5. **Fixed Intervals:**  
   *Imagine you decide to drop the first egg every 10 floors (i.e. floors 10, 20, 30, …). How many drops might you need in the worst case?*

6. **Consequences of a Break in Fixed Intervals:**  
   *If the egg breaks at, say, floor 70, how many additional drops (using the second egg) might be needed to check the floors between the previous safe floor and 70?*

7. **Total Attempts in Fixed Strategy:**  
   *Combining the drops from the first egg and the subsequent linear search with the second egg, what is the worst-case total number of drops using this fixed-interval approach?*

8. **Identifying the Flaw:**  
   *Why might a fixed-interval strategy (like every 10 floors) be suboptimal for minimizing the worst-case number of drops?*  
   *(Hint: Consider that if the egg breaks very early, you may have to do many extra drops.)*

**Moving Toward an Optimized Approach**

9. **Balancing the Costs:**  
   *How might you adjust your strategy to balance the “cost” (number of drops) before and after the first egg breaks?*

10. **Idea of Decreasing Intervals:**  
    *What if instead of fixed intervals, you drop the first egg from a floor, then from a higher floor that is fewer floors away, and so on? In other words, what is the advantage of letting the interval decrease with each drop?*

11. **Designing the Drop Sequence:**  
    *Suppose your first drop is from floor x. If the egg doesn’t break, you then drop it from floor x + (x – 1), then from floor x + (x – 1) + (x – 2), and so on. What do you think is the rationale behind decreasing the interval by 1 each time?*

12. **Balancing Worst-Case Attempts:**  
    *How does this “decreasing interval” strategy ensure that regardless of which drop causes the first egg to break, the total number of drops (including the subsequent linear search with the second egg) remains balanced?*

**Mathematical Formulation**

13. **Expressing the Drop Floors:**  
    *Express the floors at which you drop the first egg in terms of an initial value x. (For example, the drops occur at floors: x, x + (x – 1), x + (x – 1) + (x – 2), …)*

14. **Total Coverage with Drops:**  
    *What is the formula for the sum of these increments? (Recall that the sum of the first n natural numbers is n·(n + 1)/2.)*

15. **Ensuring Full Coverage:**  
    *How does the sum x + (x – 1) + (x – 2) + … + 1 relate to the total number of floors (100) you need to cover?*

16. **Setting Up the Inequality:**  
    *Write the inequality that ensures the drop sequence covers all 100 floors. (Hint: x·(x + 1)/2 ≥ 100)*

17. **Solving for x:**  
    *Solve the inequality x·(x + 1)/2 ≥ 100 to find the smallest integer value of x that works. What value of x do you obtain?*

**Application and Worst‑Case Analysis**

18. **Sequence of Floors:**  
    *Using the value of x determined above, what are the exact floors from which you would drop the first egg?*  
    *(For example, if x = 14, then the drops are from floor 14, 14 + 13 = 27, 27 + 12 = 39, etc.)*

19. **First Egg Breaks Immediately:**  
    *If the first egg breaks on the very first drop (floor x), how many total drops will have been used in the worst case (including the linear search with the second egg)?*

20. **First Egg Breaks Later:**  
    *If the egg survives several drops and then breaks on the kth drop, how many drops (first egg drops plus subsequent second egg drops) will be used in the worst-case scenario?*

21. **Consistency of Worst-Case Count:**  
    *Explain why, in this strategy, the total number of drops (k drops with egg one plus up to (x – k) drops with egg two) always equals x in the worst case.*

**Verification and Optimality**

22. **Covering All Floors:**  
    *How does the chosen sequence of drop floors (with decreasing intervals) guarantee that all 100 floors are covered without exceeding x drops?*

23. **No Better Strategy:**  
    *Why can’t you achieve a worst-case total drop count lower than the value of x you calculated?*  
    *(Hint: Consider what would happen if you tried a smaller starting value.)*

24. **Key Assumptions:**  
    *What assumptions about the eggs (for example, that each egg behaves identically and once broken cannot be used) are critical to the validity of this strategy?*

**Synthesis and Explanation**

25. **Summarizing the Strategy:**  
    *In one or two sentences, explain how the “decreasing interval” (or decremental) strategy works and why it minimizes the worst-case number of drops for determining the threshold floor in a 100‑story building with two eggs.*

---

### **What the Learner Should Discover**

By working through these questions, the learner will uncover that:
- With one egg, the worst-case is 100 drops; two eggs allow us to trade off a risky “skip” phase (using the first egg) with a careful linear search (using the second egg).
- Using a decreasing interval (first drop at floor x, then x + (x – 1), etc.) ensures that no matter when the first egg breaks, the sum of drops used will be at most x.
- Solving the inequality x·(x + 1)/2 ≥ 100 leads to x = 14, which means that in the worst case you need 14 drops.
- This step-by-step reasoning shows why 14 is the minimum number of attempts required in the worst case.
""",
    'solution': """We can skip some floors and jump ahead when testing with the first egg (egg1). Whenever egg1 breaks, egg2 has to scan linearly from
the last safe floor to the floor where egg1 broke.

For example, we can test floors 10, 15, 20 and so on. Suppose egg1 broke at the 20th floor, now we need to test from 16 to 19, which can
be done one by one using the second egg (egg2). But this is suboptimal, because regardless of when egg1 breaks, egg2 is always taking
4 attempts. We can improve this algorithm by reducing the length of the gap on each attempt of egg1.

For instance, if we test at floor 10, 10+9, 10+9+8, and so on, then in the worst case, the number of attempts will be at-most (1+9)=10 or
(2+8)=10 and so on... But, there's a problem, this sequence ends at 10 + 9 + 8... = *n*(n+1)/2 = 55 and does not span the entire
range of 100 floors. But the idea is in the right direction.

A solution for minimum steps in the worst case is the smallest integer greater than or equal to the positive solution of *x* · (*x*+1)/2 =
100  ==>  *x* = 13.651

Start at floor 14, if the egg breaks start linearly from 1, if it does not break then drop the egg from 14 + 13 = 27th floor, and so on. The
following table can be constructed.

| Egg1 Attempt | JumpSize | Egg1 Floor | Egg2 max attempts | Total Attempts |
|--------------|----------|------------|-------------------|----------------|
| 1            | 14       | 14         | 13                | 14             |
| 2            | 13       | 27         | 12                | 14             |
| 3            | 12       | 39         | 11                | 14             |
| 4            | 11       | 50         | 10                | 14             |
| 5            | 10       | 60         | 9                 | 14             |
| 6            | 9        | 69         | 8                 | 14             |
| 7            | 8        | 77         | 7                 | 14             |
| 8            | 7        | 84         | 6                 | 14             |
| 9            | 6        | 90         | 5                 | 14             |
| 10           | 5        | 95         | 4                 | 14             |
| 11           | 4        | 99         | 3                 | 14             |
| 12           | 1        | 100        | 0                 | 12             |

This ensures at-most 14 attempts.
"""
},
{'question': """Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. Now, do you want to pick door No. 2? What is the probability to win the car if you switch?""",
 'question_title': "Monty Hall Problem",
 'example_problems': """
 **Phase 1: Establishing the Basics**

1. **Initial Choice Probability:**  
   *Before any door is opened, if you pick one door out of three (with 1 car and 2 goats), what is the probability that your chosen door hides the car?*

2. **Complementary Probability:**  
   *Given your answer to Question 1, what is the probability that the car is behind one of the two doors you did not pick?*

3. **Host’s Role – Information Aspect:**  
   *After you choose a door, the host (who knows what’s behind each door) always opens one of the remaining doors to reveal a goat. Does this action change the probability that your originally chosen door contains the car? Why or why not?*

4. **Host’s Options When You Choose the Car:**  
   *If your initial choice happens to be the car (with probability 1/3), what options does the host have for opening a door?*

5. **Host’s Options When You Choose a Goat:**  
   *If your initial choice is a goat (with probability 2/3), how many doors can the host choose from, and which door will he reveal?*

**Phase 2: Exploring the Consequences of the Host’s Action**

6. **Interpreting the Host’s Reveal:**  
   *When the host reveals a goat behind one of the two doors you didn’t choose, what does that tell you about the remaining unopened door?*

7. **Scenario Breakdown – Two Cases:**  
   *Consider two cases: (a) Your initial door had the car, and (b) Your initial door had a goat. How does the outcome of switching differ in these two cases?*

8. **Switching Outcome:**  
   *In which of the two scenarios (from Question 7) does switching to the remaining door result in winning the car?*

9. **Overall Switching Probability:**  
   *Given the probabilities from Questions 1 and 2 and your analysis in Question 8, what is the overall probability of winning the car if you always switch?*

10. **Intuition vs. Calculation:**  
    *Many people think that once one door is opened, there are two doors left and each must have a 50/50 chance. Why is this intuition misleading?*

**Phase 3: Creating a Complete Picture Through Examples and Tables**

11. **Constructing a Table:**  
    *List all possible scenarios for the placement of the car (behind Door 1, 2, or 3) along with your initial pick (say, Door 1). For each scenario, note which door the host would open.*

12. **Interpreting the Table – Direct Outcomes:**  
    *From your table, identify in which cases switching would lead you to the car.*

13. **Counting Winning Scenarios:**  
    *How many of the total possible scenarios result in a win when you switch? Express this as a fraction of the total number of scenarios.*

14. **Summarizing the Outcomes:**  
    *How does the table confirm that switching wins the car in 2 out of 3 possible cases?*

15. **Host’s Knowledge Impact:**  
    *How does the fact that the host knows where the car is (and always avoids it) affect the analysis of the problem?*

**Phase 4: Deepening the Analysis**

16. **Conditional Probability Insight:**  
    *How can you describe the probability of winning by switching in terms of the chance that your initial pick was wrong?*

17. **Restating the Key Observation:**  
    *If switching wins only when your first guess is a goat, what is the probability that switching gives you the car?*

18. **Comparing to a Modified Game:**  
    *Imagine a version of the game where the host randomly opens one of the remaining doors without checking what’s behind it. How might this change the probabilities?*

19. **Importance of the Host’s Rule:**  
    *Why is it essential that the host always opens a door with a goat, rather than choosing randomly?*

20. **Generalization Thought Experiment:**  
    *Now, suppose instead of 3 doors, there are 100 doors with 1 car and 99 goats. If you pick one door and then the host opens 98 doors (all showing goats), what is the probability that switching to the one remaining closed door wins you the car?*

**Phase 5: Synthesizing and Concluding**

21. **Linking the Extreme Case to the Original Problem:**  
    *How does the extreme (100-door) case help clarify why switching is beneficial in the 3-door scenario?*

22. **Revisiting the Core Reasoning:**  
    *In your own words, explain why the probability of your initial choice being wrong remains unchanged even after the host opens a door.*

23. **Conditional vs. Unconditional Probability:**  
    *How does the host’s action serve as a “filter” that transforms the unconditional probabilities (1/3 and 2/3) into conditional ones that favor switching?*

24. **Strategic Summary:**  
    *If you had to advise someone on whether to switch or stay, based solely on the probabilities you’ve worked out, what would you say and why?*

25. **Final Synthesis:**  
    *Based on all the questions and your reasoning so far, what is the final probability of winning the car if you switch doors?*

Tthe learner should conclude that:
- **Your initial chance of picking the car is 1/3,** so there’s a 2/3 chance it is behind one of the other doors.
- **Since the host always reveals a goat,** switching essentially gives you the car whenever your initial pick was wrong.
- **Therefore, switching wins the car with probability 2/3.**
""",
'solution': """The probability that your initial choice did not have a car is indeed 2/3.

**Initial Misstep:** After one door is opened, there are exactly two doors left, and one of them has a car. So the probability that the car is behind either door is 1/2. This is incorrect because the host knows which door has a car and which door has a goat. The host always opens a door with a goat.

**Correct Solution:** The following table shows which Door the host might open. Assume that the car is behind Gate #1, and we randomly choose one door.

| Initial choice: | Door #1   | Door #2 | Door #3 |
| --------------- | --------- | ------- | ------- |
| Reality         | Car       | Goat    | Goat    |
| Host opens:     | #2 or #3 | #3      | #2      |
| Remaining:      | #3 or #2 | #1      | #1      |
| Good to switch: | No        | Yes     | Yes     |

We see that at the end, the remaining unopened door is Door #1 if we start with Door #2 or Door #3. This means that in 2 out of 3 cases, we started with the incorrect Door (#2 or #3) and we got the option to switch with the correct door at the end (#1).

So you should switch to the other door, and win the car with a probability of 2/3

**Generalization**

The probability of being initially wrong is the same as the probability of being correct after switching. We can generalize this to *n* doors. The probability of winning the game by switching after the host has opened *n* - 2 doors is (1 - 1/*n*)
"""},
{'question': """A motorboat going downstream overcame a raft at a point A; T = 60 min later it turned back and after some time passed the raft at a distance l = 6.0 km from the point A. Find the flow velocity assuming the duty of the engine to be constant.""",
 'question_title': "Irodov First Question",
 'example_problems': """
## Understanding Relative Motion

1.  **Relative Motion Basics:** If you are in a car moving at 50 km/h and throw a ball forward at 10 km/h (relative to you), what is the ball’s speed relative to the ground? *Answer: 60 km/h*

2.  **Downstream Motion:** When a boat travels downstream in a river with current *s*, how do its speed in still water (*v*) and the river’s speed *s* combine to give its effective speed relative to the bank? *Answer: v + s*

3.  **Upstream Motion:** Similarly, when the boat travels upstream, how are *v* and *s* combined to determine its effective speed relative to the bank? *Answer: v - s*

4.  **Raft’s Motion:** A raft drifts with the river’s current. What is its speed relative to the bank, and why? *Answer: s, because it moves only with the river's current.*

5.  **Reference Frame Shift:** Imagine you are standing on the raft. In this reference frame, how would you describe the river’s motion and the boat’s motion? *Hint: In the raft frame, the river is “removed” and the boat’s speed becomes its speed in still water, *v*.* *Answer: The river is not moving. The boat is moving downstream at speed *v* and upstream at speed *v*.*

## Analyzing the Boat’s Journey in the Raft’s Reference Frame

6.  **Boat’s Relative Speed:** In the raft’s frame, if the boat’s speed in still water is *v*, what is its speed relative to the raft when moving either downstream or upstream? *Answer: v*

7.  **Motion When Going Downstream:** The boat travels downstream from point A for a time *T* (60 minutes, or 1 hour). In the raft’s frame, what distance does the boat cover in that time? *Answer: vT*

8.  **Turning Point and Return:** After time *T* the boat turns around. In the raft’s frame, if the boat maintains speed *v*, how long will it take to return to the raft? *Answer: T (time = distance/speed = vT/v = T)*

9.  **Time Symmetry Insight:** What does the previous answer imply about the time it takes to go downstream (time *T*) versus the time to return upstream (call it *t₁*) in the raft’s frame? *Answer: T = t₁*

## Linking the Raft’s Motion to the Given Distance

10. **Total Drift Time:** From the bank’s point of view, the raft is moving continuously at speed *s*. If the boat meets the raft again after a total time of *T + t₁*, what is the total time that the raft has been drifting? *Answer: T + t₁*

11. **Raft’s Drift Distance:** Write an expression for the distance the raft covers (relative to the bank) during this total drift time. *Answer: s(T + t₁)*

12. **Connecting to the Problem:** The problem states that at the time of the second meeting the raft is 6.0 km downstream from point A. How can you relate this 6.0 km to your expression from question 11? *Answer: s(T + t₁) = 6.0 km*

13. **Equation for the Current:** Set up the equation that relates the river’s flow velocity *s* to the total time *(T + t₁)* and the given distance of 6.0 km. *Answer: s(T + t₁) = 6.0 km*

14. **Solving in the Raft Frame:** Solve your equation from question 13 for *s* in terms of *T* and the distance (6.0 km). *Hint: If you deduced in question 9 that *t₁ = T*, then the total time is *2T*. *Answer: s = 6.0 km / (2T)*

## Examining the Situation from the Ground (Riverbank) Frame

15. **Downstream Speed (Ground Frame):** What is the boat’s effective speed downstream relative to the bank? *Answer: v + s*

16. **Distance Covered Downstream:** Given that the boat travels downstream for time *T*, express the distance it covers (relative to the bank) in terms of *v* and *s*. *Answer: (v + s)T*

17. **Upstream Speed (Ground Frame):** After turning, what is the boat’s effective speed upstream relative to the bank? *Answer: v - s*

18. **Distance Covered Upstream:** If the boat takes a time *t₁* to meet the raft after turning, write an expression for the distance it covers upstream. *Answer: (v - s)t₁*

19. **Net Displacement of the Boat:** Write an expression for the boat’s net displacement from point A at the moment it meets the raft again, using your answers to questions 16 and 18. *Answer: (v + s)T - (v - s)t₁*

20. **Equating Positions:** At the moment of the second meeting, the boat and raft are at the same point. Write an equation that sets the boat’s net displacement equal to the raft’s displacement (which is *s* times the total time). *Answer: (v + s)T - (v - s)t₁ = s(T + t₁)*

21. **Simplification Using Time Symmetry:** Simplify your equation from question 20. What does it reveal about the relationship between *T* and *t₁*? *Answer:  (v+s)T - (v-s)t₁ = sT + st₁ => vT + sT - vt₁ + st₁ = sT + st₁ => vT = vt₁ => T = t₁*

## Final Calculation and Conclusion

22. **Total Drift Time (Revisited):** Based on your result in question 21, what is the total time the raft has been drifting? *Answer: T + t₁ = 2T = 2 hours*

23. **Raft’s Total Distance Equation:** Write the final equation for the raft’s total distance in terms of *s* and the total drift time. *Answer: s(2T) = 6.0 km*

24. **Solving for *s*:** Solve the equation from question 23 using the given distance of 6.0 km to find the numerical value of *s*. *Answer: s = 6.0 km / (2 * 1 hour) = 3.0 km/hr*

25. **Final Answer:** What is the flow velocity of the river in km/hr? *Answer: 3.0 km/hr*
""",
 'solution': """Okay, here's the analysis of the motorboat-raft problem from both reference frames, written in simple markdown:

# Motorboat-Raft Problem: Two Perspectives

## 1. Raft's Reference Frame

In this view, the raft is still. We're only concerned with the boat's motion relative to the raft.

### Key Points:

*   **Boat's Speed:** The boat's speed is *v* (its speed in still water) in both directions (upstream and downstream).
*   **Equal Times:** The time to go downstream (*T*) is the same as the time to return upstream (*t₁*). Since *T* = 1 hour, then *t₁* = 1 hour.
*   **Raft's Movement (from ground view):** Even though the raft is "still" in this frame, it drifts 6.0 km in a total time of *T + t₁* = 2 hours.

### Calculation:

Raft speed (*s*) = Distance / Time = 6.0 km / 2 hours = 3.0 km/hr

## 2. Ground (Bank) Reference Frame

Now, we see everything from the riverbank. Both the boat and raft are moving.

### Key Points:

*   **Boat's Downstream Speed:** *v + s*
*   **Boat's Upstream Speed:** *v - s*
*   **Raft's Speed:** *s*
*   **Distances:**
    *   Distance downstream: *(v + s)T*
    *   Distance upstream: *(v - s)t₁*
    *   Distance raft travels: *s(T + t₁)* = 6.0 km

### Setting up the Equation:

The boat's net displacement (downstream distance - upstream distance) equals the raft's displacement:

*(v + s)T - (v - s)t₁ = s(T + t₁)*

### Solving:

Simplify the equation: *vT + sT - vt₁ + st₁ = sT + st₁*  This cancels down to *vT = vt₁*, which means *T = t₁* (again, 1 hour).

Now use the raft's displacement: *s * (2 hours) = 6.0 km*

Therefore, *s* = 3.0 km/hr

## Conclusion

Both the raft's frame and the ground frame give the same answer:

**The river's flow velocity (s) = 3.0 km/hr**
"""},
{'question': """A point traversed half the distance with a velocity v0. The remaining part of the distance was covered with velocity v1 for half the time, and with velocity v2 for the other half of the time. Find the mean velocity of the point averaged over the whole time of motion.""",
 'question_title': "Irodov Second Question",
 'example_problems': """
## Define Average Velocity and Set Up the Problem

1. **Definition of Average Velocity:** What is the definition of average velocity in terms of total distance and total time?  *Hint:* ⟨v⟩ = Total Distance / Total Time

2. **First Half of the Journey – Time Calculation:** The first half of the distance is s/2 and is traversed at speed *v₀*. Write an expression for the time *t₁* taken to cover this part.  *Answer:* t₁ = s/(2v₀)


## Analyze the Second Half of the Journey

3. **Description of the Second Half:** The remaining half of the distance (s/2) is covered in two equal time intervals. If the duration of each interval is *t*, what is the total time for the second half? *Answer:* 2t

4. **Distances Covered in Each Interval:** In the first interval of duration *t* the speed is *v₁*, so the distance covered is *v₁t*. Similarly, in the second interval the distance is *v₂t*.

5. **Setting Up the Distance Equation for the Second Half:** Write an equation expressing that the sum of the distances in these two intervals equals s/2. *Answer:* v₁t + v₂t = s/2

6. **Solve for *t*:** Factor out *t* and solve the equation for *t* in terms of *s*, *v₁*, and *v₂*. *Answer:* t = s/(2(v₁+v₂))

7. **Total Time for the Second Half:** Express the total time for the second half, 2t, using your expression for *t*. *Answer:* 2t = s/(v₁+v₂)


## Combine and Compute the Average Velocity

8. **Total Time for the Entire Journey:** Write an expression for the total time T<sub>total</sub> as the sum of the time for the first half (t₁) and the second half (2t). *Answer:* T<sub>total</sub> = t₁ + 2t = s/(2v₀) + s/(v₁+v₂)

9. **Expressing the Average Velocity:** Substitute the total distance *s* and the total time T<sub>total</sub> into the average velocity formula. *Answer:* ⟨v⟩ = s/ (s/(2v₀) + s/(v₁+v₂))

10. **Simplify the Expression:** Cancel the common factor *s* in the numerator and denominator and simplify the resulting expression to solve for ⟨v⟩.


## Derive the Final Expression

11. **Simplification Steps:** Write the denominator as a single fraction:  s/(2v₀) + s/(v₁+v₂) = s(1/(2v₀) + 1/(v₁+v₂)). Thus, ⟨v⟩ = 1/(1/(2v₀) + 1/(v₁+v₂)).

12. **Taking the Reciprocal:** Combine the terms in the denominator: 1/(2v₀) + 1/(v₁+v₂) = (v₁+v₂ + 2v₀)/(2v₀(v₁+v₂)). Taking the reciprocal gives: ⟨v⟩ = 2v₀(v₁+v₂)/(v₁+v₂+2v₀)


## Summary

- The time to cover the first half of the distance is t₁ = s/(2v₀).
- The time to cover the second half (divided equally in time) is 2t = s/(v₁+v₂).
- The overall average velocity is ⟨v⟩ = 2v₀(v₁+v₂)/(v₁+v₂+2v₀).
""",
 'solution': """Let s be the total distance traversed by the point and t1 the time taken to cover half the distance. Further, let 2t be the time to cover the rest half of the distance.

Therefore s/2 = v0t1

or t1 = s/2v0 …(1)

And s/2 = (v1 + v2)t

Or 2t = s/(v1 + v2) …(2)

Hence the sought average velocity

<v> = s/t1 + 2t

= s/([s/2v0] + [s/(v1 + v2)])

= 2v0(v1 + v2)/(v1 + v2 + 2v0)"""},
]
