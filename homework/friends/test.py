import unittest
from friends import *


class TestFriendship(unittest.TestCase):

    def prepareUsers(self):
        '''
        Pop the test data
        '''
        self.userList = []
        self.relationshipManager = RelationshipManager()
        for i in range(10):
            user = self.relationshipManager.createUser(str(i))
            self.userList.append(user)

        relationships = [
            [0, 1, Relationship.FRIEND],
            [1, 2, Relationship.FRIEND],
            [0, 2, Relationship.FRIEND],
            [2, 3, Relationship.FRIEND]
        ]

        for relationship in relationships:
            self.relationshipManager.buildRelationship(
                self.userList[relationship[0]], self.userList[relationship[1]], Relationship.FRIEND)

    def testHasRelationship_1(self):
        """
        Test out the scenario that two peers have some relationship
        """
        self.prepareUsers()
        self.assertEqual(
            self.relationshipManager.hasRelationship(
                self.userList[0], self.userList[2]),
            True)
        assertTrue

    def testHasRelationship_2(self):
        """
        Test out the scenario that two peers have no relationship
        """
        self.prepareUsers()
        self.assertEqual(
            self.relationshipManager.hasRelationship(
                self.userList[0], self.userList[9]),
            False)

    def testGetFriends(self):
        """
        Test out retriving list of friends from the graph
        """
        self.prepareUsers()
        # print(self.relationshipManager.getFriends(self.userList[0]))
        resultDict = self.relationshipManager.getFriends(self.userList[0])
        # print(resultDict)
        self.assertSetEqual(set(resultDict.keys()), {0, 1, 2})
        self.assertSetEqual(
            set([user.username for user in resultDict[0]]), {'0'})
        self.assertSetEqual(
            set([user.username for user in resultDict[1]]), {'1','2'})
        self.assertSetEqual(
            set([user.username for user in resultDict[2]]), {'3'})

        for tier in resultDict:
            print("\ntier " + str(tier))  # ,end=" : ")
            for user in resultDict[tier]:
                print(user.username)  # ,end=" ")

        None exist user


if __name__ == '__main__':
    unittest.main()
