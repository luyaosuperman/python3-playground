#!/usr/bin/python
# -*- coding: latin-1 -*-
print("test1")
a = 1
def fun(a):
  a = 2
fun(a)
print(a)

print("\n")
print("test2")
b=[]
def fun1(b):
  b.append(1)
fun1(b)
print(b)

print("\n")
print("test3")
a=1
def fun(a):
	print("func_in",id(a))
	a=2
	print("re-point",id(a),id(2))

print("func_out",id(a),id(1))
fun(a)
print(a)

print("\n")
print("test4")
a=[]
def fun(a):
	print("func_in",id(a))
	a.append(1)
	print("re-point",id(a))

print("func_out",id(a))
fun(a)
print(a)


print("\n")
print("test5")
class Person:
	name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print(p1.name)
print(p2.name)
print(Person.name)



print("\n")
print("test6")
class Person:
	name=[]

p1=Person()
p2=Person()
p1.name.append("bbb")
print(p1.name)
print(p2.name)
print(Person.name)


print("\n")
print("test7")
class Person1:
	def __init__(self):
		self.name=[]

p1=Person1()
p2=Person1()
p1.name.append("bbb")
p2.name.append("ccc")
print(p1.name)
print(p2.name)
#non exist print(Person1.name)

print("\n")
print("test8")
print(type(p1), type(p2), type(Person1))


print("\n")
print("test9")
dict=(("1","a"), ("2","b"))
d={key:value for (key,value) in dict}
print(d)

print("\n")
print("test10")
class MyClass():
	def __init__(self):
		self.__superprivate="Hello"
		self._semiprivate=",world"

myClass = MyClass()
print("{0} {1}".format(myClass._MyClass__superprivate,myClass._semiprivate))


print("\n")
print("test11")
mylist = [1,2,3]
for i in mylist:
	print(i)

mylist = [x*x for x in range(3)]
for i in mylist:
	print(i)

mygenerator = (x*x for x in range(3))
for i in mygenerator:
	print(i)
print("--")
for i in mygenerator:
	print(i)
#nothing will print

print("\n")
print("test12")
def createGenerator():
	mylist = range(3,6)
	for i in mylist:
		yield i*i

mygenerator=createGenerator()
print(mygenerator)
for i in mygenerator:
	print(i)

print("\n")
print("test13")
import itertools
horses = [1,2,3,4]
races = itertools.permutations(horses)
print(races)
print(list(itertools.permutations(horses)))


print("\n")
print("test14")
def makebold(fn):
	def wrapped():
		print("before")
		result = "<b>" + fn() + "</b>"
		print("after")
		return result
	return wrapped
	

@makebold
def hello():
	print("inside hello")
	return "hello world"

print(hello())


print("\n")
print("test15")

def print_everything(*args):
	for count, thing in enumerate(args):
		print ('{0}. {1}'.format(count,thing))

print_everything('apple','banana','cabbage')


print("\n")
print("test16")

def table_things(**kwargs):
	for name, value in kwargs.items():
		print('{0} = {1}'.format(name, value))

table_things(apple = 'fruite', cabbage = 'vegetable')


print("\n")
print("test17")

print(map(lambda x: x*x, [y for y in range(3)]))

print("\n")
print("test18")

a = [1,2,3,4,5,6,7]
b = filter(lambda x: x>5, a)
print(b)


print("\n")
print("test19")

import copy
a = [1,2,3,4,['a','b', ['c','d']]]

b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(5)
a[4][2].append('e')
print("a = {0}".format(a))
print("b = {0}".format(b))
print("c = {0}".format(c))
print("d = {0}".format(d))


























