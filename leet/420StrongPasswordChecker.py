import unittest
class Solution(unittest.TestCase):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        #if len(s) < 6 or len(s) > 20:
        #   return False

        less = 0
        if len(s) < 6:
            less = 6-len(s)

        more = 0
        if len(s) > 20:
            more = len(s) - 20

        hasLow   = 0
        hasUpper = 0
        hasDigit = 0
        sumExtra = 0
        sumExtraBeyond = 0
        #toReplace = 0
        #toReplaceSum = 0
        repeat = 0
        preChar = ''
        one = 0
        two = 0
        three = 0

        for c in s:
            if c.islower():
                hasLow = 1

            if c.isupper():
                hasUpper = 1

            if c.isdigit():
                hasDigit = 1

            #print("c %s, preChar %s" % ( c, preChar ))
            if c == preChar:
                repeat += 1
                #print("repeat",c,repeat)
            else:
                if repeat >= 2: # start from 0
                    extra = (repeat + 1) //3
                    sumExtra += extra

                    #toReplace = (repeat + 1) % 3
                    #toReplaceSum += toReplace
                    if (repeat + 1) % 3 == 0:
                        one += 1

                    if (repeat + 1) % 3 == 1:
                        two += 1
                    if (repeat + 1) % 3 == 2:
                        three += 1

                repeat = 0
            #if c.islower() or c.isupper() or c.isdigit():
            #    preChar = c
            #else:
            #    preChar = ""
            preChar = c


        if repeat >= 2: # start from 0
            extra = (repeat + 1) //3
            sumExtra += extra

            #toReplace = (repeat + 1) % 3 + 1
            #toReplaceSum += toReplace

            if (repeat + 1) % 3 == 0:
                one += 1

            if (repeat + 1) % 3 == 1:
                two += 1

            if (repeat + 1) % 3 == 2:
                three += 1


        change = 3-hasLow-hasUpper-hasDigit
        print('\n\n',s, 
            "less", less, 
            "more", more, 
            "sumExtra", sumExtra, 
            "change",change, 
            "one", one,
            "two", two,
            "three", three,
            hasLow, hasUpper, hasDigit)
        
        if less > 0:
            return max(sumExtra, less,change)

        if more > 0:
            sumExtra -= min(more,one)
            sumExtra -= min(max(more-one,0), two * 2) // 2
            sumExtra -= max(more - one - 2*two, 0) // 3
            return more + max(change,sumExtra)
        
        return max(sumExtra, change)
            


    def test_1(self):
        self.assertEqual(self.strongPasswordChecker(""), 6)

    def test_2(self):
        self.assertEqual(self.strongPasswordChecker("aaaaaa1"), 2)

    def test_3(self):
        self.assertEqual(self.strongPasswordChecker("aaa111"), 2)

    def test_4(self):
        self.assertEqual(self.strongPasswordChecker("ABABABABABABABABABAB1"), 2)    

    def test_5(self):
        self.assertEqual(self.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa"), 7)    

    def test_6(self):
        self.assertEqual(self.strongPasswordChecker("..."), 3)    

    def test_7(self):
        self.assertEqual(self.strongPasswordChecker("1234567890123456Baaaaa"), 3)  

    def test_8(self):
        self.assertEqual(self.strongPasswordChecker("..................!!!"), 7)  

    def test_9(self):
        self.assertEqual(self.strongPasswordChecker("aaaabbaaabbaaa123456A"), 3)  

    def test_10(self):
        self.assertEqual(self.strongPasswordChecker(""), 6)  

if __name__ == '__main__':
    unittest.main()
