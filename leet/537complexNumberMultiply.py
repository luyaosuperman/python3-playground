import unittest

class Solution(unittest.TestCase):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        #print("a:{0}".format(a))
        ra = int(a.split("+")[0])
        ia = int(a.split("+")[1][:-1])
        #print("ra:{0} ia:{1}".format(ra,ia))

        #print("b:{0}".format(b))
        rb = int(b.split("+")[0])
        ib = int(b.split("+")[1][:-1])
        #print("rb:{0} ib:{1}".format(rb,ib))

        return "{0}+{1}i".format(
        	str(ra*rb - ia*ib),
        	str(ra*ib + rb*ia))


    def test_1(self):
    	inputs = [["1+1i", "1+1i"],]
    	outputs = ["0+2i"]
    	for i in range(len(outputs)):
    		self.assertEqual(
    			self.complexNumberMultiply(
    				inputs[i][0], inputs[i][1]), 
    			outputs[i])


if __name__ == '__main__':
	unittest.main()
