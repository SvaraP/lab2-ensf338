
"""
Q1: What is a profilier, and what does it do?

    A profiler is a tool that helps programmers monitor the performance of their code. Essentially it takes 
    "statistics" (basically it times the code) to see how it compares to the rest of the code. Which serves 
    to determine what is taking an longer to complete and which parts of your code needs to be opptimized.

Q2: How does profiling differ from benchmarking?

    Profiling compares the time each section of the code needs to complete its task, benchmarking is equivalent
    to comparing different versions of code (all serving the same end goal) to see which performs better overall.
    For example, profiling is like seeing which section of an assignment is taking the longest to do whereas
    benchmarking is like comparing the time it takes to do assignments in general.
"""



import cProfile as profile 

import timeit
def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]
    
test_function()
third_function()


print("Profiling test_function")
profile.run('test_function()')

print("\nProfiling third_function")
profile.run('third_function()')

