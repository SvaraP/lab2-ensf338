## 1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan [0.5 pts]
    The algorithm I would use is a Binary-Linear Search hybrid. I would first use the Binary Search method to split the rooms into categories of "EY100-130" and "All other rooms", then I would use Linear Search to check every room I pass.

## 2. How many ”steps” it will take to find room EY128? And what is a “step” in this case? [0.25 pts]
    With this algorithm, it will take 15 steps to find EY128. 
    In this case, each "step" represents movement to the next room.
    
## 3. Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts]
    It is neither, because we do not find EY128 on our first or last step.

## 4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like [0.5 pts]
    The worst-case scenario would be the room we are looking for taking the most steps. So our worst-case would be look for EY300.
    The best-case scenario would be the room we are looking for being the first room we check. So our best-case would be looking for EY100 or EY138.

## 5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient? [0.5 pts]
    If I had the layout memorized, I would split the rooms into four sections EY100-108 (left), EY110-118 (top left), EY120-128 (top right) and EY130-138 (right). Then based on the room number, I would immediately know which quadrant I would need go to and once in that quadrant, I could use LinearSearch to find my desired room.
