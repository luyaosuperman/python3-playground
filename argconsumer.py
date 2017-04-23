#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

#arg consumer
import sys
print(len(sys.argv), type(sys.argv))
for count,arg in enumerate(sys.argv):
    print("{0} -> {1}".format(count,arg))

print(""" "\"\" """)
print( 17/3, 17//3, 5**2)

str1 = "012345"
print(str1)
print(str1[0])
print(str1[-1])
print(str1[2:3])
print(str1[2:])
print(str1[:3])

print(str1[-2:])
print(str1[:-2])

print(str1[999:])

print(3*r'\n')
print([0,1] + [2,3])

a,b=0,1
while (b<10):
    print(b, end=",")
    a,b = b, a+b

print('\n')
"""
x=0
while x!=999:
    x=int(input("Please enter an interger. Exit with 999: "))

    if x<0:
        x=0
        print('Negative changed to zero')
    elif x == 0:
        print('zero')
    elif x == 1:
        print('Single')
    elif x == 999:
        print('quit loop with 999')
    else:
        print('More')
"""

words = ['cat','hamster','bird']
for w in words[:]:
    print(w,len(w))
    if len(w) > 3:
        words.insert(0,w)
print(words)



print(range(5,10))
print(range(0,10,3))
print(range(-10,-100,-30))
print(type(range(-10,-100,-30)))
print(list(range(-10,-100,-30)))
for i in range(5):
    print(i)

for i in range(0,10,3):
    print(i)

for i in range(-10,-100,-30):
    print(i)

a = ['a','b','c']
for i in range(len(a)):
    print(i, a[i])

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number: ", num)
        continue
    print("Found a odd number:   ", num)

#while True:
    #pass

class MyEmptyClass:
    pass #remember to implement this

def initlog(*args):
    pass

def fib(n):
    """print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(100)

print(fib)
f=fib
f(100)
print(f(0))

print()
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ask_ok('test',2)

i=5
def f(arg=i):
    print(arg)

i=6
f()

def f(a, L=[]):
    L.append(a)
    return L

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def function(a):
    pass

#function(0,a=0)

def cheeseshop(kind, *arguments, **keywords):
    print("kind: ", kind)
    print(*arguments, sep=" ")
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("a","b","c",
    aa1="aa",
    bb2="bb",
    cc3="cc")

def concat(*args, sep="/") -> str:
    """ concat a few strings

    Hello, concat
    """
    print("Annotations:", concat.__annotations__)
    print("Arguments:", *args, sep)

    return sep.join(args)

print(concat("a","b","c",sep=","))

args = [3,6]
print(list(range(*args)))

d = {"n":100}
fib(**d)

def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(0))
print(f(1))

print(concat.__doc__)

