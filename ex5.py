import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Linear Search method
def LinearSearchMethod(lst, x):
    for j in range(len(lst)): #iteration through array
        if lst[j] == x:
            return j #elements position number return if found
    return 0 #if the elements position number is not found, 0 will be returned

def BinarySearchMethod(lst, x):
    first = 0
    last = len(lst) - 1
    while first <= last:
        mid = int((first + last) / 2) # Finds the middle of the array
        if x == lst[mid]: # Checks if the middle element is the element that we are looking for
            return mid  
        elif x < lst[mid]: # Left half is searched if the element is still not found
            last = mid - 1
        else: # Right half is searched if the element is still not found
            first = mid + 1
    return -1

# arrays 
array1000=[1000]
array2000=[2000]
array4000=[4000]
array8000=[8000]
array16000=[16000]
array32000=[32000]

def populateArray(array):
    size = len(array)
    for i in range (size):
        array[i] = i
    return array

array1000 = populateArray(array1000)
array2000 = populateArray(array2000)
array4000 = populateArray(array4000)
array8000 = populateArray(array8000)
array16000 = populateArray(array16000)
array32000 = populateArray(array32000)



# Linear Search timming 
array1000_linearSearch = timeit.timeit(stmt="LinearSearchMethod(array1000,999)", 
                             setup="from __main__ import LinearSearchMethod, array1000", 
                             number=1000)
array2000_linearSearch = timeit.timeit(stmt="LinearSearchMethod(array2000,1999)", 
                             setup="from __main__ import LinearSearchMethod, array2000", 
                             number=1000)
array4000_linearSearch = timeit.timeit(stmt="LinearSearchMethod(array4000,3999)", 
                             setup="from __main__ import LinearSearchMethod, array4000", 
                             number=1000)
array8000_linearSearch = timeit.timeit(stmt="LinearSearchMethod(array8000,7999)", 
                             setup="from __main__ import LinearSearchMethod, array8000", 
                             number=1000)
array16000_linearSearch = timeit.timeit(stmt="LinearSearchMethod(array16000,15999)", 
                             setup="from __main__ import LinearSearchMethod, array16000", 
                             number=1000)
array32000_linearSearch = timeit.timeit(stmt="LinearSearchMethod(array32000,31999)", 
                             setup="from __main__ import LinearSearchMethod, array32000", 
                             number=1000)
Average_LinearSearch = (array1000_linearSearch + array2000_linearSearch + array4000_linearSearch + array16000_linearSearch + array8000_linearSearch + array32000_linearSearch)/6
print ("Average linear search: " + str(Average_LinearSearch))

# Binary Search timimg 
array1000_BinarySearch = timeit.timeit(stmt="BinarySearchMethod(array1000,999)", 
                             setup="from __main__ import BinarySearchMethod, array1000", 
                             number=1000)
array2000_BinarySearch = timeit.timeit(stmt="BinarySearchMethod(array2000,1999)", 
                             setup="from __main__ import BinarySearchMethod, array2000", 
                             number=1000)
array4000_BinarySearch = timeit.timeit(stmt="BinarySearchMethod(array4000,3999)", 
                             setup="from __main__ import BinarySearchMethod, array4000", 
                             number=1000)
array8000_BinarySearch = timeit.timeit(stmt="BinarySearchMethod(array8000,7999)", 
                             setup="from __main__ import BinarySearchMethod, array8000", 
                             number=1000)
array16000_BinarySearch = timeit.timeit(stmt="BinarySearchMethod(array16000,15999)", 
                             setup="from __main__ import BinarySearchMethod, array16000", 
                             number=1000)
array32000_BinarySearch = timeit.timeit(stmt="BinarySearchMethod(array32000,31999)", 
                             setup="from __main__ import BinarySearchMethod, array32000", 
                             number=1000)
Average_BinarySearch = (array1000_BinarySearch + array2000_BinarySearch + array4000_BinarySearch + array16000_BinarySearch + array8000_BinarySearch + array32000_BinarySearch)/6
print ("Average Binary search: " + str(Average_BinarySearch))




# Data points to be used by the plot
array_sizes = np.array([1000, 2000, 4000, 8000, 16000, 32000])
linear_search_times = np.array([array1000_linearSearch, array2000_linearSearch, array4000_linearSearch, array8000_linearSearch, array16000_linearSearch, array32000_linearSearch])
binary_search_times = np.array([array1000_BinarySearch, array2000_BinarySearch, array4000_BinarySearch, array8000_BinarySearch, array16000_BinarySearch, array32000_BinarySearch])

# functions for curve fitting
#AI use declaration for helping fix the formulas (line 105 to 111)
def linear_function(x, a, b):
    return a * x + b 
linear_params, _ = curve_fit(linear_function, array_sizes, linear_search_times)

def logarithmic_function(x, c, d):
    return c * np.log(x) + d
binary_params, _ = curve_fit(logarithmic_function, array_sizes, binary_search_times)

# Plotting:
plt.scatter(array_sizes, linear_search_times, color='blue', label='Linear Search Times')
plt.plot(array_sizes, linear_function(array_sizes, *linear_params), color='red', label='Interpolated Linear Function')
plt.xlabel('Size Of Array')
plt.ylabel('Time (s)')
plt.title('Linear Search')
plt.legend()
plt.show()

plt.scatter(array_sizes, binary_search_times, color='green', label='Binary Search Times')
plt.plot(array_sizes, logarithmic_function(array_sizes, *binary_params), color='orange', label='Interpolated Logarithmic Function')
plt.xlabel('Size Of Array')
plt.ylabel('Time (s)')
plt.title('Binary Search')
plt.legend()
plt.show()













"""
Linear Search:
    * Works by sequentially iterating through an array to locate a specific element.
    * Time complexity increases linearly as the size of the array increases because it needs to check each element one by one.
Binary Search:
    * Utilizes a divide-and-conquer approach to locate a specific element by halving the search area over and over.
    * It has way quicker search time when compared to Linear Search because of its logarithmic time complexity.
     this causes is way less comparissons in binary search to locate the target element.
Comparison:
    * The output of the code showcases that the average time it takes for a Binary Search is less than that of Linear Search.

"""
