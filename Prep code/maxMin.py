#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    # Write your code here
    k -= 1
    arr.sort()
    i = 0
    n = len(arr)
    minimum = arr[k] - arr[i]
    # minIndex = i
    # maxIndex = k
    while i + k < n:
        if minimum > arr[i + k] - arr[i]:
            minimum = arr[i + k] - arr[i]
            # minIndex = i
            # maxIndex = i+k
        i += 1
    return minimum


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + "\n")

    fptr.close()
