#!/usr/bin/python3
import unittest

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b



class Solution(unittest.TestCase):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if (len(points) <= 2):
            return len(points)

        maxResult = 0;

        for i in range(len(points)):
            duplicate = 0
            vertical = 0
            slopeDict = {}
            maxResultPoint = 0
            for j in range(i+1, len(points)):
                #print ("i {0} j {1}".format(i, j))

                #detect vertical and duplicate
                if points[i].x == points[j].x:
                    if points[i].y == points[j].y:
                        duplicate += 1
                    else:
                        vertical += 1
                    continue;

                #detect slope rate, in x and y

                deltax = points[i].x - points[j].x
                deltay = points[i].y - points[j].y
                gcd = self.getGcd(abs(deltay),abs(deltax));
                if (gcd > 0):
                    deltay /= gcd
                    deltax /= gcd

                if deltax < 0:
                    deltax *= -1
                    deltay *= -1


                if (deltay,deltax) in slopeDict:
                    slopeDict[(deltay,deltax)] += 1
                else:
                    slopeDict[(deltay,deltax)] = 1
            if len(slopeDict) > 0:
                maxResultPoint = \
                    max(vertical, slopeDict[max(slopeDict, key=slopeDict.get)])
                #print(slopeDict)
                #print("max count from maxResultPoint:", maxResultPoint)
            maxResultPoint =max(maxResultPoint,vertical)
            #print("vertical:", vertical)
            maxResultPoint += duplicate + 1
            #print("duplicate:", duplicate)
            #print("maxResultPoint:", maxResultPoint)
            #print("------")



            maxResult = max(maxResultPoint, maxResult)

        return maxResult


    def getGcd(self,a,b):
        while b:
            a, b = b, a%b;
        return a;


    def test_1(self):
        points = [Point(0,0), Point(1,1), Point(2,2)];
        self.assertEqual(self.maxPoints(points), 3)

    def test_2(self):
        points = [Point(0,0), Point(1,1), Point(1,-1)]
        self.assertEqual(self.maxPoints(points), 2)

    def test_3(self):
        points = [Point(0,0), Point(-1,-1), Point(2,2)]
        self.assertEqual(self.maxPoints(points), 3)

if __name__ == '__main__':
    unittest.main()