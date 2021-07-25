#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    pm_or_am = s[-2:]
    if pm_or_am == "AM":
        modified_hour = int(s[:2])
        modified_hour = modified_hour % 12
        modified_hour = str(modified_hour)
        modified_hour = '0' + modified_hour
        s = modified_hour + s[2:-2]
        return s
    else:
        modified_hour = int(s[:2])
        modified_hour = modified_hour % 12 + 12
        modified_hour = str(modified_hour)
        s = modified_hour + s[2:-2]
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

    # timeConversion("07:00:00PM")
