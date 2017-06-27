
class TrieNode():

    def __init__(self, value, isRoot=False):
        self.nextTrieNode = dict()
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

        self.nextTrieNode[nextChar] = TrieNode(value)

    def addWord(self, value):
        assert(len(value) >= 1)
        char = value[0]
        assert(char == self.value)
        if len(value) == 1:
            self.count += 1
            return
        else:
            value = value[1:]
            nextChar = value[0]

        if nextChar in self.nextTrieNode:
            self.nextTrieNode[nextChar].addWord(value)
        else:
            self.nextTrieNode[nextChar] = TrieNode(value)

    def getWord(self, value, isRoot=False):


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
