import unittest

debugPrint = False  # only print if it is True
stackPrint = True


def xPrint(*args):
    """
    A print function that can be turned on/off
    """
    if debugPrint:
        print(*args)


def printStack(method):
    """
    print the name of the method
    """
    def printed(*args, **kw):
        if stackPrint:
            xPrint("****", method.__name__, args, kw)
        result = method(*args, **kw)
        if stackPrint:
            xPrint("++++", method.__name__, args, kw, "Returns", result)
        return result
    return printed


class TrieNode():

    @printStack
    def __init__(self, value, isRoot=False):
        self.nextTrieNodes = dict()
        assert(len(value) >= 1)
        char = value[0]
        if isRoot == False:
            self.char = char
            if len(value) == 1:
                self.count = 1
                return
            else:
                self.count = 0
                value = value[1:]
                nextChar = value[0]
        else:
            nextChar = char

        self.nextTrieNodes[nextChar] = TrieNode(value)

    @printStack
    def addWord(self, value, isRoot=False):
        assert(len(value) >= 1)
        char = value[0]
        if isRoot == True:
            nextChar = char
        else:
            assert(char == self.char)
            if len(value) == 1:
                self.count += 1
                return
            else:
                value = value[1:]
                nextChar = value[0]

        if nextChar in self.nextTrieNodes:
            self.nextTrieNodes[nextChar].addWord(value)
        else:
            self.nextTrieNodes[nextChar] = TrieNode(value)

    @printStack
    def getWord(self, value, partial=False, isRoot=False):
        assert(len(value) >= 1)
        char = value[0]
        if isRoot == True:
            if char in self.nextTrieNodes:
                return self.nextTrieNodes[char].getWord(value, partial)
            else:
                return False
        else:
            if len(value) == 1:
                if char == self.char and (partial == True or self.count >= 1):
                    return True
                else:
                    return False
            else:
                value = value[1:]
                nextChar = value[0]
                if nextChar not in self.nextTrieNodes:
                    return False
                else:
                    return self.nextTrieNodes[nextChar].getWord(value, partial)

    def printStack(self, isRoot=False, level=0):
        if isRoot == True:
            xPrint("root")
            xPrint(self.nextTrieNodes)
        else:
            xPrint(level, self.char, self.count)
            xPrint(self.nextTrieNodes)
        for nextChar in self.nextTrieNodes:
            self.nextTrieNodes[nextChar].printStack(level=level + 1)


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    @printStack
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if self.root == None:
            self.root = TrieNode(word, isRoot=True)
        else:
            self.root.addWord(word, isRoot=True)

        self.root.printStack(isRoot=True)

    @printStack
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if self.root == None:
            return False
        else:
            return self.root.getWord(word, isRoot=True)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if self.root == None:
            return False
        else:
            return self.root.getWord(prefix, partial = True, isRoot=True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class UnitTest(unittest.TestCase):

    def test1(self):
        trie = Trie()
        self.assertEqual(trie.search("abc"), False)
        words = ["abc", "abde", "abfg","zxvf","dsfcxsrwecsdf"]
        for word in words:
            trie.insert(word)

        # trie.search("def")

        for word in words:
            self.assertEqual(trie.search(word), True)

        self.assertEqual(trie.startsWith("ab"), True)
        self.assertEqual(trie.startsWith("z"), True)
        self.assertEqual(trie.startsWith("d"), True)
        self.assertEqual(trie.startsWith("e"), False)

if __name__ == '__main__':
    unittest.main()
