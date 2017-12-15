#!/bin/python3

import sys

def aVeryBigSum(n, ar):
  # Complete this function
  result = 0
  for item in ar:
    result += item
  return result

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
