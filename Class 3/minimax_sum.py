#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# store min sum and max sum, arr = 5 elements
"""
def miniMaxSum(arr):
    arr.sort()
    # newArr = sorted(arr)
    minSum = arr[:4]
    minTotal = 0
    for i in minSum:
        minTotal = minTotal + i
    
    maxSum = arr[1:]
    maxTotal = 0
    for i in maxSum:
        maxTotal = maxTotal + i
    print (f'{minTotal} {maxTotal}')
"""


def miniMaxSum(arr):
    arr.sort()
    s = sum(arr)
    minSum = s - arr[-1]
    maxSum = s - arr[0]
    print(minSum, maxSum)


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
