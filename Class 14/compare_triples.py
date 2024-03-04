#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    # Write your code here
    answer = [0, 0]
    for i in range(0, 3):
        if a[i] < b[i]:
            answer[1] += 1
        elif a[i] > b[i]:
            answer[0] += 1
        else:
            pass
    return answer


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # a = list(map(int, input().rstrip().split()))
    # b = list(map(int, input().rstrip().split()))
    a = [5, 6, 7]
    b = [3, 6, 10]

    result = compareTriplets(a, b)
    print(result)

    # fptr.write(" ".join(map(str, result)))
    # fptr.write("\n")

    # fptr.close()
