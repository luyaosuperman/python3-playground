l = ['a','b','c','a']
print(l.count('a'))
print(l.count('d'))

print(l.index('a'))
print(l.index('a',1))

print(l.reverse())
print(l)
l.append('e')
l.sort()
print(l)
print(l.pop())
print(l)

print("-----------------")

stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["a","b","c"])
queue.append("d")
queue.append("e")
print(queue.popleft())
print(queue.popleft())
print(queue)


print("-----------------")


squares = list(map(lambda x: x**2, range(10)))
print(squares)
print([x**2 for x in range(3)])

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y])

print("-----------------")
vec = [-4,-2,0,2,4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

l = [' a ',' b ',' c ']
print([i.strip() for i in l])

print([(x, x**2 ) for x in range(6)])

vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi,i)) for i in range(1,6)])

print("-----------------")

matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
]

print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))

a=[0,1,2,3,4,5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

a=[0,1,2,3,4,5]
a1,a2,a3,a4,a5,a6 = a
print(a1,a2,a3)


print("-----------------")

s = {'a','b','c'}
print(s)
print('a' in s)
print('d' in s)

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

print(s1)
print(s2)

print(s2-s1)
print(s2|s1)
print(s2&s1)
print(s2^s1)

print("-----------------")
#d= {[]:1}
#TypeError: unhashable type: 'list'

d= {"a":1, "b":2}
print(d)
print(d["a"])
del d["b"]
print(d)
print(dict([("a",1),("b",2)]))

d= {"a":1, "b":2}
for k,v in d.items():
	print(k,v)

print(enumerate(["a","b",'c']))
for i,v in enumerate(["a","b",'c']):
	print(i,v)

l1 = ["a","b","c"]
l2 = ["aa","bb","cc"]

for i1,i2 in zip(l1,l2):
	print("{0} {1}".format(i1,i2))

for i in reversed(range(1,10,2)):
	print(i)

for i in sorted(set(["3","5","7","1"])):
	print(i)

for i in set(["3","5","7","1"]):
	print(i)

s1,s2,s3="","a","b"
print(s1 or s2 or s3)