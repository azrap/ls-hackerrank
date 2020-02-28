#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibonacci' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def fibonacci(n):
    # Write your code here
    if n < 2:
        return [0]
    array = []
    sum = 0
    count = 2
    n1 = 0
    n2 = 1
    array.append(n1)
    array.append(n2)
    while count < n:
        sum = n1+n2
        array.append(sum)
        n1 = n2
        n2 = sum
        count += 1

    return array
