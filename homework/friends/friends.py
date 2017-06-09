import unittest
import random

class User():
    '''
    User information class
    Node in the relationship graph
    it stores the relationship/edge of the graph
    '''
    def __init__(self, username):
        self.username = username
        self.relationshipList = []


    def addRelationship(self, relationship):
        '''
        store the relationship in the user/node
        Adjacency list
        '''
        self.relationshipList.append(relationship)

    '''def getFriends(self):
        return [relationship 
                for relationship in self.relationshipList 
                and relationship.isFriend()]

    def getPartners(self):
        return [relationship 
                for relationship in self.relationshipList 
                and relationship.isPartner()]

    def getParents(self):
        return [relationship 
                for relationship in self.relationshipList 
                and relationship.isParent()]

    def getChilds(self):
        return [relationship 
                for relationship in self.relationshipList 
                and relationship.isChild()]'''

    def getPeers(self):
        '''
        return the list of peers whoever has any relationship with the user
        '''
        return self.relationshipList


########################################
class Relationship():
    '''
    relationship of two users/edge of the graph
    relationship is directional. 
    e.g. user1 --parent--> user2 
    and  user2 --child---> user1
    '''

    FRIEND  = 1
    PARTNER = 2
    PARENT  = 4
    CHILD   = 8
    #can only be one

    def __init__(self, user1, user2, relationshipType):
        '''
        relaionshipType should be the one of 
        user1-->user2
        the other direction will be managed by code
        '''
        self.user1 = user1
        self.user2 = user2
        self.relationshipType = relationshipType
        self._anotherRelationship()


    def _anotherRelationship(self):
        '''
        build the relationship of the other direction
        '''
        if (self.relationshipType == Relationship.FRIEND or 
                self.relationshipType == Relationship.PARTNER):
            self.anotherRelationshipType = self.relationshipType

        elif self.relationshipType == Relationship.PARENT:
            self.anotherRelationshipType = Relationship.CHILD

        elif self.relationshipType == Relationship.CHILD:
            self.anotherRelationshipType = Relationship.PARENT
        else:
            raise RuntimeError("I canot find another relationship for you")

    def getPeer(self, user):
        '''
        get the other user of this relationship
        '''
        if user == self.user1:
            return self.user2
        elif user == self.user2:
            return self.user1
        else:
            raise RuntimeError("The user queried does not exist in this relationship")

    '''def _getRelationship(self, user):
        if user == self.user1:
            return self.relationshipType
        elif user == self.user2:
            return self.anotherRelationshipType
        else:
            raise RuntimeError("The user queried does not exist in this relationship")

    def isFriend(self, user):
        return self._getRelationship(user) == Relationship.FRIEND

    def isPartner(self, user):
        return self._getRelationship(user) == Relationship.PARTNER

    def isParent(self, user):
        return self._getRelationship(user) == Relationship.PARENT

    def isChild(self, user):
        return self._getRelationship(user) == Relationship.CHILD'''

class RelationshipManager():
    '''
    relationships and users are managed here.
    create user here,
    find relationship here as well.
    '''
    def __init__(self):
        self.userList = []

    def createUser(self, username):
        '''
        create a new user
        '''
        user = User(username)
        self.userList.append(user)
        return user

    def buildRelationship(self, user1, user2, relationshipType):
        '''
        Link up user1 and user2
        '''
        relationship = Relationship(user1, user2, relationshipType)
        user1.addRelationship(relationship)
        user2.addRelationship(relationship)

    '''def descripeRelationship(self, user, maxTier = -1):
        pass

    def describeFamily(self, user):
        pass'''

    def hasRelationship(self, user1, user2):
        '''
        check if there is any relationship between user1 and user2

        DFS version
        '''
        if user1 not in self.userList or user2 not in self.userList:
            raise RuntimeError("one or more user doe not exist")

        result = False
        visited = [False] * len(self.userList)
        stack = []
        stack.append(user1)# stack top is at the end of the list
        while len(stack) > 0:
            user = stack.pop() #remove and return the last item

            if user == user2:
                result = True
                break

            visited[self.userList.index(user)] = True
            for relationship in user.getPeers():
                nextUser = relationship.getPeer(user)
                if visited[self.userList.index(nextUser)] == False:
                    stack.append(nextUser)

        return result


class Test(unittest.TestCase):

    def prepareUsers_1(self):
        '''
        Pop the test data
        '''
        self.userList = []
        self.relationshipManager = RelationshipManager()
        for i in range(10):
            user = self.relationshipManager.createUser(str(i))
            self.userList.append(user)

        self.relationshipManager.buildRelationship(
            self.userList[0],self.userList[1], Relationship.FRIEND)
        self.relationshipManager.buildRelationship(
            self.userList[1],self.userList[2], Relationship.FRIEND)


    def test_1(self):
        self.prepareUsers_1()
        self.assertEqual(
            self.relationshipManager.hasRelationship(self.userList[0], self.userList[2]), 
            True)

        
    def test_2(self):
        self.prepareUsers_1()
        self.assertEqual(
            self.relationshipManager.hasRelationship(self.userList[0], self.userList[3]), 
            False)


if __name__ == '__main__':
    random.seed(1)
    unittest.main()






