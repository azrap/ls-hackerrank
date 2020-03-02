#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'threeNumberSum' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#


def threeNumberSum(arr, target):
    # Write your code here
    arr.sort()
    triplets = []
    n = len(arr)
    idx = 0

    dict_ele = dict()
    # store all elements in a hashtable first
    while idx < n:
        dict_ele[arr[idx]] = idx
        idx += 1

    # fix the ith element arr[i]
    for i in range(0, n):

        # are there any pairs with (sum1+sum2)=target-arr[i]? if so, can utilize the 2sum strategy from sprint
        sum_of_2 = target-arr[i]

        for num1 in arr:
            # making sure we don't double count arr[i]
            if num1 != arr[i]:
                num2 = sum_of_2-num1
                # making sure we don't double count arr[i] and num1
                # aslo checking to see if num2 is in the dict
                if num2 != num1 and num2 != arr[i] and num2 in dict_ele:
                    # if it is, that means we've found a triplet
                    triplet = [arr[i], num1, num2]
                    triplet.sort()
                    triplets.append(triplet)

    # deduping the triplets:
    sol = []
    for t in triplets:
        if t not in sol:
            sol.append(t)
    return sol
