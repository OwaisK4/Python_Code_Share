#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    colors = {}
    for i in range(n):
        if ar[i] not in colors:
            colors[ar[i]] = 1
            # print("Created a key", ar[i])
        else:
            colors[ar[i]] += 1
            # print("Incremented a key", ar[i])
        # print(colors)
    # print(colors)
    pairs = 0
    for key in colors:
        # print(colors[key])
        pairs += colors[key] // 2
    print(pairs)
    return pairs


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    # ar = list(map(int, input().rstrip().split()))
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()
