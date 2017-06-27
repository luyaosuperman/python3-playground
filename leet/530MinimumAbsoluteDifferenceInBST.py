#!/usr/bin/python3
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(unittest.TestCase):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        bucket = []

        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            value = node.val
            if value in bucket:
                return 0
            else:
                bucket.append(value)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

        bucket.sort()
        print(bucket)
        minimal = bucket[-1]
        for i in range(1, len(bucket)):
            if abs(bucket[i] - bucket[i-1]) < minimal:
                minimal = abs(bucket[i] - bucket[i-1])

        return minimal

    def test1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(self.getMinimumDifference(root), 1)

if __name__ == '__main__':
    unittest.main()