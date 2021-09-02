#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.


def add(frequencies, query):
    if query[1] not in frequencies:
        frequencies[query[1]] = 1
    else:
        frequencies[query[1]] += 1


def delete(frequencies, query):
    if query[1] in frequencies:
        if frequencies[query[1]] == 1:
            frequencies.pop(query[1])
        else:
            frequencies[query[1]] -= 1


def check(frequencies, query):
    for integer in frequencies:
        if frequencies[integer] == query[1]:
            return 1
    return 0


def freqQuery(queries):
    frequencies = {}
    command_map = {1: add, 2: delete, 3: check}
    results = []
    for query in queries:
        result = command_map[query[0]](frequencies, query)
        if result == 0 or result == 1:
            results.append(result)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
