import random
import timeit


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
# Linear Search timming 
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
















"""
The interpolated funtion specifically the linear function fits to the linear graph and reveals a consistent, linear increase, whre time frows proportionally 
to the size of the array. The log function fits the binary data because the search time increases as the array size expands, 
overall the interpolated functions accurately visual representation of their respective complexities.
"""
