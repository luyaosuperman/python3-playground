#!/usr/bin/python3
import unittest

# Definition for a point.
class Point(unittest.TestCase):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)

        result = list();
        word = list()
        for c in reversed(l):
            if c == " ":


                result += reversed(word);
                word = list()

                if(len(result) == 0 or 
                    #leading space
                    len(result) > 0 and result[-1] == " "):
                    #duplicate space
                    continue

                result.append(" ")

            else:
                word.append(c)
        #print(word)
        result += reversed(word);
        #print(result)

        if len(result) > 0 and result[-1] == " ":
            return "".join(result[:-1])
        else:
            return "".join(result)



        
    def test_1(self):
        inputString = "the sky is blue";
        outputString = "blue is sky the";

        self.assertEqual(self.reverseWords(inputString), outputString)
    
    def test_2(self):
        inputString = " 1";
        outputString = "1";

        self.assertEqual(self.reverseWords(inputString), outputString)

    def test_2(self): #corner case
        inputString = "";
        outputString = "";

        self.assertEqual(self.reverseWords(inputString), outputString)



if __name__ == '__main__':
    unittest.main()