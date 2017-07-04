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
            xPrint("++", method.__name__, args, kw)
        result = method(*args, **kw)
        if stackPrint:
            xPrint("--", method.__name__, args, kw, "Returns", result)
        return result
    return printed


class TrieNode():

    @printStack
    def __init__(self, char="", count=0, isRoot=False):
        self.nextTrieNodes = dict()
        self.char = char
        self.count = count
        self.isRoot = isRoot


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(isRoot=True)

    @printStack
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        chars = list(word)
        currentNode = self.root
        while(len(chars) > 0):
            xPrint(chars)
            char = chars[0]
            if currentNode.isRoot:
                nextChar = char
                xPrint("root")
            else:
                xPrint("None root")
                chars.pop(0)
                if len(chars) == 0:
                    currentNode.count += 1
                    return None
                else:
                    nextChar = chars[0]

            if nextChar not in currentNode.nextTrieNodes:
                currentNode.nextTrieNodes[nextChar] = TrieNode(nextChar)

            xPrint(currentNode.nextTrieNodes.keys())
            currentNode = currentNode.nextTrieNodes[nextChar]

    @printStack
    def __search(self, word, partial=False):
        chars = list(word)
        currentNode = self.root

        xPrint("word", word)
        xPrint("chars", chars)
        while(len(chars) > 0):
            xPrint("*************")
            xPrint("chars", chars)
            char = chars[0]
            if currentNode.isRoot:
                nextChar = char
                xPrint("root")
            else:
                xPrint("None root")
                chars.pop(0)
                xPrint("currentNode.count", currentNode.count)
                if len(chars) == 0:

                    xPrint("partial", partial)
                    xPrint(currentNode.nextTrieNodes.keys())
                    if currentNode.count > 0 or partial:
                        return True
                    else:
                        return False
                else:
                    nextChar = chars[0]

            xPrint("nextChar in currentNode.nextTrieNodes",
                   nextChar in currentNode.nextTrieNodes)
            xPrint("nextChar", nextChar)
            xPrint(currentNode.nextTrieNodes.keys())
            if nextChar in currentNode.nextTrieNodes:
                currentNode = currentNode.nextTrieNodes[nextChar]
            else:
                return False

    @printStack
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.__search(word, partial=False)

    @printStack
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.__search(prefix, partial=True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class UnitTest(unittest.TestCase):

    #@unittest.skip
    @printStack
    def test1(self):
        trie = Trie()
        self.assertEqual(trie.search("abc"), False)
        words = ["g", "abc", "abde", "abfg", "zxvf", "dsfcxsrwecsdf"]
        for word in words:
            trie.insert(word)

        # trie.search("def")

        for word in words:
            self.assertEqual(trie.search(word), True)

        self.assertEqual(trie.startsWith("ab"), True)
        self.assertEqual(trie.startsWith("z"), True)
        self.assertEqual(trie.startsWith("d"), True)
        self.assertEqual(trie.startsWith("e"), False)

    #@unittest.skip
    @printStack
    def test2(self):
        actions = [
            'Trie',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'insert',
            'search',
            'search',
            'search',
            'search',
            'startsWith',
            'startsWith',
            'startsWith',
            'startsWith',
        ]
        data = [
            [],
            ['aaaaa'
             ],
            ['aaaab'
             ],
            ['aaaac'
             ],
            ['aaaad'
             ],
            ['aaaae'
             ],
            ['aaaaf'
             ],
            ['aaaag'
             ],
            ['aaaah'
             ],
            ['aaaai'
             ],
            ['aaaaj'
             ],
            ['aaaak'
             ],
            ['aaaal'
             ],
            ['aaaam'
             ],
            ['aaaan'
             ],
            ['aaaao'
             ],
            ['aaaap'
             ],
            ['aaaaq'
             ],
            ['aaaar'
             ],
            ['aaaas'
             ],
            ['aaaat'
             ],
            ['aaaau'
             ],
            ['aaaav'
             ],
            ['aaaaw'
             ],
            ['aaaax'
             ],
            ['aaaay'
             ],
            ['aaaaz'
             ],
            ['aaaa'
             ],
            ['aaab'
             ],
            ['aaac'
             ],
            ['aaad'
             ],
            ['aaae'
             ],
            ['aaaf'
             ],
            ['aaag'
             ],
            ['aaah'
             ],
            ['aaai'
             ],
            ['aaaj'
             ],
            ['aaak'
             ],
            ['aaal'
             ],
            ['aaam'
             ],
            ['aaan'
             ],
            ['aaao'
             ],
            ['aaap'
             ],
            ['aaaq'
             ],
            ['aaar'
             ],
            ['aaas'
             ],
            ['aaat'
             ],
            ['aaau'
             ],
            ['aaav'
             ],
            ['aaaw'
             ],
            ['aaax'
             ],
            ['aaay'
             ],
            ['aaaz'
             ],
            ['aaaaa'
             ],
            ['aaaaaa'
             ],
            ['aaaa'
             ],
            ['a'],
            ['aaaaa'
             ],
            ['aaaaaa'
             ],
            ['aaaa'
             ],
            ['a'],
        ]
        expected = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            True,
            False,
            True,
            False,
            True,
            False,
            True,
            True,
        ]

        assert(len(actions) == len(data))
        assert(len(actions) == len(expected))

        trie = Trie()
        for action, dat, expect in zip(actions, data, expected):
            if action == "Trie":
                pass
            if action == "insert":
                trie.insert(dat[0])
            if action == "search":
                self.assertEqual(trie.search(dat[0]), expect)
            if action == "startsWith":
                self.assertEqual(trie.startsWith(dat[0]), expect)

    @printStack
    def test3(self):
        actions = [
            'Trie',
            'insert',
            'insert',
            'insert',
            'insert',
            'search',
            'search',
            'search',
            'search',
            'startsWith',
            'startsWith',
            'startsWith',
            'startsWith',
        ]
        data = [
            [],
            ['aaaaa'],
            ['aaaaz'],
            ['aaaa'],
            ['aaaz'],
            ['aaaaa'],
            ['aaaaaa'],
            ['aaaa'],
            ['a'],
            ['aaaaa'],
            ['aaaaaa'],
            ['aaaa'],
            ['a'],
        ]
        expected = [
            None,
            None,
            None,
            None,
            None,
            True,
            False,
            True,
            False,
            True,
            False,
            True,
            True,
        ]

        assert(len(actions) == len(data))
        assert(len(actions) == len(expected))

        trie = Trie()
        for action, dat, expect in zip(actions, data, expected):
            if action == "Trie":
                pass
            if action == "insert":
                trie.insert(dat[0])
            if action == "search":
                self.assertEqual(trie.search(dat[0]), expect)
            if action == "startsWith":
                self.assertEqual(trie.startsWith(dat[0]), expect)


if __name__ == '__main__':
    unittest.main()
