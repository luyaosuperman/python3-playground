import os
print(os.getcwd())
'''os.chdir('/tmp/')
try:
    os.system('mkdir today')
except Exception as err:
    print(err)
'''
print(dir(os))

import glob
print(glob.glob('*.py'))

import sys
print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')
