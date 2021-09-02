#!/bin/python3

import math
import os
import random
import re
import sys


def most_common_characters(name):
    occurrences = {}
    for character in sorted(name):
        if character not in occurrences:
            occurrences[character] = 0
        occurrences[character] += 1
    ordered_occurrences = dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True))
    # ordered_occurrences = dict(sorted(ordered_occurrences.items(), key=lambda item: item[0]))
    prints = 0
    for key, value in ordered_occurrences.items():
        prints += 1
        print(key + " " + str(value))
        if prints == 3:
            break


if __name__ == '__main__':
    s = input()
    most_common_characters(s)
