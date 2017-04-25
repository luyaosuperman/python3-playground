import fibo

fibo.fib(100)
print(fibo.__name__)

fib = fibo.fib
fib(10)

import importlib
importlib.reload(fibo)

from fibo import fib, fib2
fib(50)

import sys
print(sys.path)
print(dir(sys))

print()
#print(sys.ps1) interactive only
#print(sys.ps2) interactive only
sys.path.append("/root")

print()
import builtins
print(dir(builtins))