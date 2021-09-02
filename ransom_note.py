#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def checkMagazine(magazine, note):
    word_dictionary = {}
    if len(note) > len(magazine):
        print("No")
        return
    for word in magazine:
        word_dictionary[word] = 0
    for word in magazine:
        word_dictionary[word] += 1
    for word in note:
        if word not in word_dictionary:
            print("No")
            return
        if word_dictionary[word] == 0:
            print("No")
            return
        word_dictionary[word] -= 1
    print("Yes")
    return


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
