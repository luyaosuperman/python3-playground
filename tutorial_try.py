'''
while True:
	try:
		x = int(input("A number: "))
		break
	except (ValueError, NameError, TypeError):
		print("Oops, not a valid number.")
'''

class B(Exception):
	pass

class C(B):
	pass

class D(C):
	pass


for cls in [B,C,D]:
	try:
		raise cls();
	except D:
		print("D")
	except C:
		print("C")
	except B:
		print("B")

import sys
try:
	f = open('nonexist','r')
	s = f.readline()
	i = int(s.strip())
#except OSError as err:
#	print("OS error: {0}".format(err))
except ValueError:
	print("Could not convert data to an integer")
except:
	print("Unhandled error: ", sys.exc_info()[0])
	print(sys.exc_info())
	#raise

for arg in sys.argv[1:]:
	try:
		f=open(arg, 'r')
	except OSError:
		print('cannot open', arg)
	else:
		print(arg, ' has ', len(f.readlines()), ' lines' )
		f.close()

print("=======")
try:
	raise Exception('spam','eggs')
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)

	x, y = inst.args
	print("x=", x)
	print("y=", y)

print("========")
def this_fails():
	x = 1/0

try:
	this_fails()
except ZeroDivisionError as err:
	print("Handling run-time error: ",err)

class Error(Exception):
	"""base class for exceptions"""
	pass

class InputError(Error):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

class TransitionError(Error):
	def __init__(self, previous, next, message):
		self.previous = previous,
		self.next = next
		self.message = message

try:
	raise KeyboardInterrupt
finally:
	print('Goodbye, world!')

def divide(x,y):
	try:
		result = x/y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print("result is", result)
	finally:
		print("executing finally clause")

divide(2,1)
divide(2,0)
divide("2","1")
'''
>>> divide("2","1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
'''