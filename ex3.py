
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

Q3: Use a profiler to measure execution time of the program(skip function definitions).

    Answered in the code that is provided 

Q4: Discuss a sample output. Where does execution time go?

    The output of a profiler includes the number of function calls (ncalls) which depicts the number of times that 
    the function was called. It allows for a differentiation between the total number of calls and the number of 
    primitive calls. Primitive calls are called that are not due to recursion, the way I remember it is that primitive
    is the way primal/ initial contacts. Then there is the total time (totime) which is the time that the code spends executing the code. 
    After that we have the cumulative time (cumtime) which is the cumulative time that the functon spends in all of the functions. Basically
    if a function calls itself then the cumtime is indicative of the time in the back and forth as well. Next there is 
    the per call time (percall) which is the average time spent percall to the function. Which is calculated by the total 
    time divided by the number of calls (totime/ ncalls). Finally we have the filename and te line number (filename:lineno(function))
    this essentially identifies in the output what the location of the source code is and where the function is defined.

    Essentially, the key takeaways are as follows:
    - ncalls = number of calls 
    - totime = total time 
    - cumtime = cumulative time 
    - percall = per call time 
    - filename:lineno(function) = filename and line number 
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

