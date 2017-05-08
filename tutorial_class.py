def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		global spam
		spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment: ", spam)

	do_nonlocal()
	print("after nonlocal assignment: ", spam)

	do_global()
	print("after global assignment: ", spam)

scope_test()
print("In global scope: ", spam)

class MyClass(int):
	'''A Simple Class'''
	i = 12345

	def f(self):
		return 'hello world'

x = MyClass()

class Complex:

	a=1

	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart
		self.a=2

x = Complex(3.0, -4.5)
print(x.r, x.i, x.a, Complex.a)

x.counter = 1
while x.counter < 10:
	x.counter = x.counter * 2
print(x.counter)
del x.counter

print(isinstance(x, Complex))
print(issubclass(bool, int))

class Reverse:
	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

rev = Reverse('spam')
for char in rev:
	print(char,end='')
print()

def reverse1(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]

for char in reverse1('spam'):
	print(char,end='')
print()