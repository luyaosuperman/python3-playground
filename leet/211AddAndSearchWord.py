import unittest
import data211

debugPrint = False  # only print if it is True
stackPrint = True


def xPrint(*args):
    """
    A print function that can be turned on/off
    """
    if debugPrint:
        pass
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
        self.lenSet = set()


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(isRoot=True)

    @printStack
    def addWord(self, word):
        """
        Adds a word into the data structure.
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
            #add after possible pop
            currentNode.lenSet.add(len(chars))

            if nextChar not in currentNode.nextTrieNodes:
                currentNode.nextTrieNodes[nextChar] = TrieNode(nextChar)

            xPrint(currentNode.nextTrieNodes.keys())
            currentNode = currentNode.nextTrieNodes[nextChar]

    @printStack
    def __search(self, word):
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

                    xPrint(currentNode.nextTrieNodes.keys())
                    if currentNode.count > 0:
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
    def __bfs(self, word):
        chars = list(word)
        currentNode = self.root
        qChars = []
        qNodes = []
        qChars.append(chars)
        qNodes.append(self.root)

        while len(qChars) > 0:
            assert(len(qChars) == len(qNodes))
            xPrint("***********")
            xPrint("qChars", qChars)
            xPrint("qNodes", qNodes)
            chars = qChars.pop(0)
            currentNode = qNodes.pop(0)
            xPrint("chars", chars)
            xPrint("currentNode", currentNode)

            if currentNode.isRoot == False:
                xPrint("None root")
                chars.pop(0)
            else:
                xPrint("root")

            if len(chars) == 0:
                xPrint("len(chars) == 0")
                xPrint("currentNode.count", currentNode.count)
                if currentNode.count > 0:
                    return True
                else:
                    # return False
                    continue
            else:
                char = chars[0]
                xPrint("char", char)

            xPrint("chars after pop: ", chars)
            xPrint(currentNode.nextTrieNodes.keys())
            if char != '.':
                if char in currentNode.nextTrieNodes:
                    xPrint("char in currentNode.nextTrieNodes")
                    qChars.append(chars[:])
                    qNodes.append(currentNode.nextTrieNodes[char])
                else:
                    continue
            elif char == '.':
                for c in currentNode.nextTrieNodes:
                    qChars.append(chars[:])
                    qNodes.append(currentNode.nextTrieNodes[c])
            else:
                assert(False)

            # none root

            # last node
        return False

    @printStack
    def __bfs2(self, word):
        chars = list(word)
        currentNode = self.root
        qChars = []
        qNodes = []
        # qChars.append(chars)
        qChars.append(0)
        qNodes.append(self.root)

        while len(qChars) > 0:
            assert(len(qChars) == len(qNodes))
            xPrint("***********")
            xPrint("qChars", qChars)
            xPrint("qNodes", qNodes)
            #chars = qChars.pop(0)
            cursor = qChars.pop(0)
            currentNode = qNodes.pop(0)
            xPrint("chars", chars)
            xPrint("currentNode", currentNode)


            if currentNode.isRoot == False:
                xPrint("None root")
                # chars.pop(0)
                cursor += 1
            else:
                xPrint("root")

            if len(set(chars[cursor:])) == 1 and chars[cursor] == '.':
                return len(chars) - cursor in currentNode.lenSet


            # if len(chars) == 0:
            if len(chars) - cursor == 0:
                xPrint("len(chars) == 0")
                xPrint("currentNode.count", currentNode.count)
                if currentNode.count > 0:
                    return True
                else:
                    # return False
                    continue
            else:
                #char = chars[0]
                char = chars[cursor]
                xPrint("char", char)

            #xPrint("chars after pop: ", chars)
            xPrint(currentNode.nextTrieNodes.keys())
            if char != '.':
                if char in currentNode.nextTrieNodes:
                    xPrint("char in currentNode.nextTrieNodes")
                    # qChars.append(chars[:])
                    qChars.append(cursor)
                    qNodes.append(currentNode.nextTrieNodes[char])
                else:
                    continue
            elif char == '.':
                for c in currentNode.nextTrieNodes:
                    # qChars.append(chars[:])
                    qChars.append(cursor)
                    qNodes.append(currentNode.nextTrieNodes[c])
            else:
                assert(False)

            # none root

            # last node
        return False

    @printStack
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.__bfs2(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class UnitTest(unittest.TestCase):

    #@unittest.skip
    @printStack
    def test1(self):
        trie = WordDictionary()
        self.assertEqual(trie.search("abc"), False)
        words = [
            "g",
            "abc",
            "abde",
            "abfg",
            "zxvf",
            "dsfcxsrwecsdf"
        ]
        for word in words:
            trie.addWord(word)

        # trie.search("def")

        for word in words:
            self.assertEqual(trie.search(word), True)

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

        trie = WordDictionary()
        for action, dat, expect in zip(actions, data, expected):
            if action == "Trie":
                pass
            if action == "insert":
                trie.addWord(dat[0])
            if action == "search":
                self.assertEqual(trie.search(dat[0]), expect)
            if action == "startsWith":
                pass
                #self.assertEqual(trie.startsWith(dat[0]), expect)

    #@unittest.skip
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

        trie = WordDictionary()
        for action, dat, expect in zip(actions, data, expected):
            if action == "Trie":
                pass
            if action == "insert":
                trie.addWord(dat[0])
            if action == "search":
                self.assertEqual(trie.search(dat[0]), expect)
            if action == "startsWith":
                pass
                #self.assertEqual(trie.startsWith(dat[0]), expect)

    #@unittest.skip
    @printStack
    def test4(self):
        trie = WordDictionary()
        trie.addWord("bad")
        trie.addWord("dad")
        trie.addWord("mad")

        self.assertEqual(trie.search("pad"), False)
        self.assertEqual(trie.search("bad"), True)
        self.assertEqual(trie.search(".ad"), True)
        self.assertEqual(trie.search("b.."), True)

    @printStack
    def test5(self):
        trie = WordDictionary()
        for action, dat in zip(
            data211.actions,
            data211.data
        ):
            if action == "WordDictionary":
                pass
            if action == "addWord":
                trie.addWord(dat[0])
            if action == "search":
                trie.search(dat[0])


    @printStack
    def test6(self):
        trie = WordDictionary()
        for action, dat, expect in zip(
            ["WordDictionary","addWord","search"],
            [[],["a"],["."]],
            [None,None,True]

        ):
            if action == "WordDictionary":
                pass
            if action == "addWord":
                trie.addWord(dat[0])
            if action == "search":
                self.assertEqual(trie.search(dat[0]), expect)


    @printStack
    def test7(self):
        trie = WordDictionary()
        for action, dat, expect in zip(
            ["WordDictionary","addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"],
            [[],["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]],
            [None,None,None,None,None,None,None,None,None,True,False,True,True,True,False,True,True,False,False]

        ):
            if action == "WordDictionary":
                pass
            if action == "addWord":
                trie.addWord(dat[0])
            if action == "search":
                self.assertEqual(trie.search(dat[0]), expect)

if __name__ == '__main__':
    unittest.main()