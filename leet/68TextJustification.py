#!/usr/bin/python3
import unittest

class Solution(unittest.TestCase):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        outputs = []
        line = []
        lineWidth = 0
        for word in words:
            #print("processing", word)
            if (len(word) + lineWidth + len(line) ) > maxWidth:
                #print(line, lineWidth)
                for i in range(maxWidth - lineWidth):
                    line[i%(len(line) - 1 or 1)] += ' '

                outputs.append(''.join(line))
                line = []
                lineWidth=0

            line.append(word)
            lineWidth += len(word)

        return outputs + [' '.join(line).ljust(maxWidth)]


    def test_1(self): #corner case
        inputs  = ["This", "is", "an", "example", "of", "text", "justification."]
        n = 16
        outputs = [
                    "This    is    an",
                    "example  of text",
                    "justification.  "
        ]

        self.assertEqual(self.fullJustify(inputs,n), outputs)



if __name__ == '__main__':
    inputs  = ["This", "is", "an", "example", "of", "text", "justification."]
    n = 16
    solution = Solution()
    print(solution.fullJustify(inputs,n))
    #unittest.main()
