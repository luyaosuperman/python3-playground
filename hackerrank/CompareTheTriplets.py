#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
  # Complete this function
  a = [a0,a1,a2]
  b = [b0,b1,b2]
  sumA = sumB = 0
  for i in range(3):
    if a[i] > b[i]:
      sumA += 1
    elif b[i] > a[i]:
      sumB += 1
    else:
      assert(a[i]==b[i])
  return (sumA, sumB)
  #print("%s %s" % (sumA, sumB))
    

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
