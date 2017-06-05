import unittest
class Solution(unittest.TestCase):
    #DP, too slow
    '''def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        #Corner cases
        #s empty, p *
        

        s=list(s)
        p=list(p)
        p=self.mergeStar(p)
        print("testing\n", s,'\n', p )

        #if len(s) == 0 and len(p) == 1 and p[0] == '*':
        #    return True

        cur_s = 0
        cur_p = 0
        while cur_s < len(s) and cur_p < len(p):
            #print("cur_s {0} s[cur_s] {1}, cur_p {2}, p[cur_p] {3}".format( cur_s, s[cur_s], cur_p, p[cur_p] ))
            if s[cur_s] == p[cur_p] or p[cur_p] == '?':
                cur_s += 1
                cur_p += 1
            elif p[cur_p] == "*":
                while cur_p + 1 < len(p) and p[cur_p+1] == "*":
                    cur_p += 1
                if cur_p == len(p)-1:
                    return True
                #at least 1 
                cur_ss = cur_s
                while cur_ss < len(s):
                    if not self.isMatch(s[cur_ss:], p[cur_p + 1:]):
                        cur_ss += 1
                    else:
                        return True
                cur_s += 1

            else:
                return False

        #print("cur_s {0} cur_p {1}".format(cur_s, cur_p))
        if cur_s == len(s) and cur_p == len(p):
            return True
        elif cur_s == len(s) and p[cur_p] == "*":
            return self.isMatch([], p[cur_p+1 : ])
        else:
            return False'''


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        #Corner cases
        #s empty, p *
        

        s=list(s)
        p=list(p)
        p=self.mergeStar(p)
        print("\n\ntesting\n", s,'\n', p )

        #if len(s) == 0 and len(p) == 1 and p[0] == '*':
        #    return True

        cur_s = 0
        cur_p = 0

        match = 0
        star = -1
        while cur_s < len(s) :
            #print("cur_s {0} s[cur_s] {1}, cur_p {2}, p[cur_p] {3}".format( cur_s, s[cur_s], cur_p, p[cur_p] ))
            if cur_p < len(p) and (s[cur_s] == p[cur_p] or p[cur_p] == '?'):
                cur_s += 1
                cur_p += 1
            elif cur_p < len(p) and p[cur_p] == "*":
                star = cur_p
                match = cur_s
                cur_p = cur_p+1
            elif (star != -1):
                #mismatch, but there is a star in the previous location
                match = match+1
                cur_s = match
                cur_p = star+1
                #out of star
                #continue on from next position
            else:
                return False

        #print("cur_s {0} cur_p {1}".format(cur_s, cur_p))
        while cur_p<len(p) and p[cur_p] == "*":
            cur_p += 1

        if cur_s == len(s) and cur_p == len(p):
            return True
        #elif cur_s == len(s) and p[cur_p] == "*":
        #    return self.isMatch([], p[cur_p+1 : ])
        else:
            return False

    def mergeStar(self, p):
        #print("before merge", p)
        result = []
        for i in range(len(p)):
            if p[i] != '*' or (p[i] == "*" and (i==len(p)-1 or p[i+1] != '*' )):
                result.append(p[i])
        #print("after merge", result)
        return result

       

    def test_1(self):
        self.assertEqual(self.isMatch("aa","a")       , False)

    def test_2(self):
        self.assertEqual(self.isMatch("aa","aa")      , True )

    def test_3(self):
        self.assertEqual(self.isMatch("aaa","aa")     , False)

    def test_4(self):
        self.assertEqual(self.isMatch("aa", "*")      , True )

    def test_5(self):
        self.assertEqual(self.isMatch("aa", "a*")     , True )

    def test_6(self):
        self.assertEqual(self.isMatch("ab", "?*")     , True )

    def test_7(self):
        self.assertEqual(self.isMatch("aab", "c*a*b") , False)

    def test_8(self):
        self.assertEqual(self.isMatch("", "*")        , True)

    def test_8_1(self):
        self.assertEqual(self.isMatch("de", "de")        , True)

    def test_9(self):
        self.assertEqual(self.isMatch("abefcdgiescdfimde", "ab*cd?i*de")        , True)

    def test_10(self):
        self.assertEqual(self.isMatch("zacabz", "*a?b*")        , False)

    def test_11(self):
        self.assertEqual(self.isMatch("a", "a*")        , True)

    def test_12(self):
        self.assertEqual(self.isMatch("ho", "ho**")        , True)

    def test_13(self):
        self.assertEqual(self.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab",
                                      "***bba**a*bbba**aab**b")        , True)

if __name__ == '__main__':
    unittest.main()
