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

def miniMaxSum(array):
    array.sort()
    min_sum = 0
    for index in range(1, len(array)-1):
        min_sum += array[index]
    max_sum = min_sum
    max_sum += array[len(array)-1]
    min_sum += array[0]
    print(str(min_sum) + " " + str(max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
