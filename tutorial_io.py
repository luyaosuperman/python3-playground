s = "Hello, world."
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
print(repr((x, y, ('spam', 'eggs'))))

for x in range(1,11):
	print(repr(x).rjust(2), repr(x**2).rjust(3), end = ' ')
	print(repr(x**3).rjust(4))

for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x,x**2,x**3))

print()
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1415926'.zfill(5))
print('We are the {} who say "{}!"'.format('knights','Ni'))
print('{0} and {1}'.format('spam','eggs'))
print('{1} and {0}'.format('spam','eggs'))
print('This {food} is {adjective}.'.format
	(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}'.format
	('Bill', 'Manfred', other='Georg'))

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

print()

import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
	print('{0:10} ==> {1:10d}'.format(name, phone))

print('Jack: {0[Jack]:d}; \nSjoerd: {0[Sjoerd]:d};\n'
	'Dcab: {0[Dcab]:d}'.format(table))

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print
f = open('workfile','w')
print(f.write("this is a test\n"))
value = ('the answer', 42)
s = str(value)
f.write(s)
f.close()
print()
f = open('workfile','r')
#print(f.read())
for line in f:
	print(line, end='')
f.close()

print("\n+++++++++++++\n")
with open('workfile','r') as f:
	for l in f.readlines():
		print(l, end='')


import json
f = open('jsontest','w')
x = [1, 'simple', ('list',)]
print(json.dumps(x))
json.dump(x,f)
f.close()

f = open('jsontest')
y = json.load(f)
print(y)
f.close()