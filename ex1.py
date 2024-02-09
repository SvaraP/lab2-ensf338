import timeit
import matplotlib.pyplot as plt
import numpy as np

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
#recursive call 
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
#4. 
#memoization and recursive call 
memo = {} # makes an empty dictionairy where memo will store it's values 

#AI use declaration (33-40)
#I used Chatgpt to help me come up with the syntax for  memoization as I couldn't find 
# find information regaurding this in the notes.
def memo_function(n):
  if n in memo:
    return memo[n] # if n already exists, return that value
  if n == 0 or n == 1:
    return n  # if n is 0 or 1, it can directly return 0 or 1 directly
  if n not in memo:
    memo[n]= func(n-1) + func(n-2) #if n value is not in memo, it's computed using recursion
    return memo [n]
  
#5. Give an expression for the time complexity of the optimized algorith:
  #time complericity expression of O(n)

#6.  
#AI use declaration for the plotting
#I used Chatgpt to help me fix the plot code as it was only plotting one value
# and kept breaking. I ran my original code through and it helped me find my mistakes and fix them
total_time_memo_function = []
total_time_func = []

for n in range(36):
    total_time_memo = timeit.timeit(stmt=f"memo_function({n})", setup="from __main__ import memo_function", number=1)
    total_time_memo_function.append(total_time_memo)
    
    total_time_recursive = timeit.timeit(stmt=f"func({n})", setup="from __main__ import func", number=1)
    total_time_func.append(total_time_recursive)

# Plotting 
plt.plot(total_time_memo_function, color='orange', marker='x', label='Memoized Function')
plt.xlabel('Value(n)')
plt.ylabel('Time (s)')
plt.title('Timming Plot for Memoized Function')
plt.legend()
plt.savefig('ex1.6.1.jpg') 
plt.show()
plt.plot(total_time_func, color='green', marker='o', label='Recursive Function')
plt.xlabel('Value (n)')
plt.ylabel('Time (seconds)')
plt.title('Timming Plot for Recursive Function')
plt.legend()
plt.savefig('ex1.6.2.jpg')  
plt.show()

