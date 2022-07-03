# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.
# URL: https://www.hackerrank.com/challenges/np-arrays/problem

import numpy


def arrays(arr):
    arr.reverse()
    arr = numpy.array(arr, float)
    return arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
