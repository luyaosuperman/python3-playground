#!/bin/python3
import sys

n = int(input().strip())
#print("n",n)
a = []
result1 = result2 = 0
for a_i in range(n):
  a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
  result1 += a_t[a_i]
  result2 += a_t[n-1-a_i]
  a.append(a_t)
print(abs(result1-result2))
#print(a)

