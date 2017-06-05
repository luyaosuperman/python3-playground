import unittest

class Solution(unittest.TestCase):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s.strip()
        try:
        	float(s)
        except:
        	return False
        else:
        	return True
       

    def test_1(self):
    	tests = [
    			 ["0"     , True ].
				 [" 0.1 " , True ],
				 ["abc"   , False],
				 ["1 a"   , False],
				 ["2e10"  , True ],
				 [".1"    , True ],
				]
    	for i in range(len(tests)):
    		self.assertEqual(
    			self.isNumber(tests[i][0]), tests[i][1])


if __name__ == '__main__':
	unittest.main()
