
debugPrint = True # only print if it is True
stackPrint = True
def xPrint(*args):
	"""
	A print function that can be turned on/off
	"""
	if debugPrint:
		print(*args)

def printStack(method):
	"""
	print the name of the method
	"""
	def printed(*args, **kw):
		if stackPrint:
			xPrint("entering", method.__name__)
		result = method(*args, **kw)
		return result
	return printed