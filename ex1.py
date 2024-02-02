# Part 1: Questions  
#1. What does this code do? [0.1 pts]

    # This section of code is the Fibonacci sequence done throught recursion.

#2. Is this an example of a divide-and-conquer algorithm (think carefully about
#this one)? [0.1 pts]

    # No this is not divide-and-conquer algorithm as it directly solved the Fibonacci sequence 
    #throught recursion and doesn't break it one into smaller sections, which are solved indeednetly and then 
    #combied to provide the final solution

#3. Give an expression for the time complexity of the algorithm [0.2 pts]
    # this is an exponential algorithm, which has a time complericity expression of O(2^n)


# provided code 

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
