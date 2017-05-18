#!/usr/bin/python3
import unittest

class Node():
    def __init__(self, key, value, pre, next):
        self.pre   = pre
        self.next  = next
        self.key   = key
        self.value = value

class LRUCache(unittest.TestCase):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count    = 0
        self.head     = Node(-1,-1,None,None)
        self.tail     = Node(-2,-2,None,None)
        self.dict     = dict()

        self.head.next = self.tail
        self.tail.pre  = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            return self.dict[key].value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        print("put", key, value, key in self.dict)
        self.trace()

        if key in self.dict:
            node = self.dict[key]
            #update value
            node.value = value

            if self.count > 1:
                #print(key, self.dict)
                #pop to front
                #edge case!!!
                node.pre.next = node.next
                node.next.pre = node.pre

                node.next = self.head.next
                node.pre = self.head

                self.head.next.pre = node
                self.head.next     = node




        else:
            #build Node
            node = Node(key, value, self.head, self.head.next)
            self.head.next.pre = node
            self.head.next = node

            self.dict[key] = node
            self.count += 1
            if self.count > self.capacity:
                #evict last one
                del self.dict[self.tail.pre.key]
                self.tail.pre = self.tail.pre.pre
                self.count -= 1

        self.trace()

    def trace(self):
        current = self.head
        i = 0
        print("++++")
        print(self.dict.keys())
        while current is not None:
            print("trace", i, current.key, current.value, current.pre, current.next)
            if current.next is not None:
                assert current.next.pre == current
            current = current.next
            i += 1
        print("++++")
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':

    '''lruCache = LRUCache(10)
    for i in range(12):
        lruCache.put(0,0)
        lruCache.put(i,i) 
        print("****************")
        for j in range(12):
            print(j,lruCache.get(j))

    print("=====================")
    for i in range(12):
        print(i,lruCache.get(i))'''

    inputs = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    lruCache = LRUCache(10)
    cache = dict()
    for i in inputs:
        if len(i) == 1:
            print("__get {0}".format(i[0]))
            lruCache.get(i[0])
        if len(i) == 2:
            print("__put {0} {1}".format(i[0], i[1]))
            lruCache.put(i[0], i[1])
            #dict[i[0]] =  i[1]


    #unittest.main()