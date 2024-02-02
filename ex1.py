# Part 1: Questions  
#1. What does this code do? [0.1 pts]
#2. Is this an example of a divide-and-conquer algorithm (think carefully about
#this one)? [0.1 pts]
#3. Give an expression for the time complexity of the algorithm [0.2 pts]
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)