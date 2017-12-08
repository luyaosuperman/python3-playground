import unittest

debugPrint = True  # only print if it is True
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


class TwitterTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        pass

####################################################


class HashMapTest(unittest.TestCase):

    def setUp(self):
        self.hashMap = HashMap()

    def tearDown(self):
        self.hashMap = None

    def test_basic(self):
        #insert first
        for i in range(100):
            self.hashMap.put(i, "->%s" % i)
            for j in range(i+1):
                self.assertEqual(
                    self.hashMap.get(j),
                    "->%s" % j
                )
            for j in range(i+1, 100):
                self.assertEqual(
                    self.hashMap.get(j),
                    None
                )

        #then delete
        for i in range(100):
            self.hashMap.delete(i)
            for j in range(i+1):
                self.assertEqual(
                    self.hashMap.get(j),
                    None
                )
            for j in range(i+1, 100):
                self.assertEqual(
                    self.hashMap.get(j),
                    "->%s" % j
                )

####################################################


class HashMap(object):

    def __init__(self):
        self.N = 0  # number of pairs
        self.M = 8  # size of linear probe table
        self.keys = [None] * self.M
        self.values = [None] * self.M
        xPrint("self.keys", self.keys)
        xPrint("self.values", self.values)

    def __hash(self, key):
        # Assume integer input. With python it is a must
        return (key & 0x7fffffff) % self.M

    @printStack
    def put(self, key, value):
        assert key != None
        assert value != None
        if self.N > self.M / 2:
            self.__resize(self.M * 2)

        i = self.__hash(key)
        xPrint("hash of key %s is %s" % (key, i))
        xPrint("self.keys[i]", self.keys[i])
        while self.keys[i] != None:
            xPrint(i, (i + 1) % self.M)
            i = (i + 1) % self.M
        self.keys[i] = key
        self.values[i] = value

        self.N += 1

    @printStack
    def get(self, key):
        assert key != None
        i = self.__hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                return self.values[i]
            i = (i + 1) % self.M
        return None

    @printStack
    def delete(self, key):
        assert key != None
        if self.get(key) == None:
            return

        i = self.__hash(key)
        while self.keys[i] != key:
            i = (i + 1) % self.M

        self.keys[i] = None
        self.values[i] = None
        i = (i + 1) % self.M

        while self.keys[i] != None:
            keyToRedo = self.keys[i]
            valueToRedo = self.values[i]

            self.keys[i] = None
            self.values[i] = None
            self.N -= 1  # otherwise later it will be duplicate value
            self.put(keyToRedo, valueToRedo)
            i = (i + 1) % self.M

        self.N -= 1
        if self.N > 0 and self.N == self.M // 8:
            self.__resize(self.M // 2)

    @printStack
    def __resize(self, __M):
        oldKeys = self.keys
        oldValues = self.values

        self.M = __M
        self.N = 0
        self.keys = [None] * self.M
        self.values = [None] * self.M

        for i in range(len(oldKeys)):
            if oldKeys[i] != None:
                self.put(oldKeys[i], oldValues[i])


####################################################

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        pass

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        pass

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        pass

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

if __name__ == '__main__':
    unittest.main()
