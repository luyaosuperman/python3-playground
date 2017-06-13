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

    def getFriends(self):
        return [relationship
                for relationship in self.relationshipList
                if relationship.isFriend(self)]

    def getPartners(self):
        return [relationship
                for relationship in self.relationshipList
                if relationship.isPartner(self)]

    def getParents(self):
        return [relationship
                for relationship in self.relationshipList
                if relationship.isParent(self)]

    def getChilds(self):
        return [relationship
                for relationship in self.relationshipList
                if relationship.isChild(self)]

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

    FRIEND = 1
    PARTNER = 2
    PARENT = 4
    CHILD = 8
    # can only be one

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
            raise RuntimeError(
                "The user queried does not exist in this relationship")

    def _getRelationship(self, user):
        """
        Return the relationship from this user to the peer
        """
        if user == self.user1:
            return self.relationshipType
        elif user == self.user2:
            return self.anotherRelationshipType
        else:
            raise RuntimeError(
                "The user queried does not exist in this relationship")

    def isFriend(self, user):
        return self._getRelationship(user) == Relationship.FRIEND

    def isPartner(self, user):
        return self._getRelationship(user) == Relationship.PARTNER

    def isParent(self, user):
        return self._getRelationship(user) == Relationship.PARENT

    def isChild(self, user):
        return self._getRelationship(user) == Relationship.CHILD


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
        visited = []
        stack = []
        stack.append(user1)  # stack top is at the end of the list
        while len(stack) > 0:
            user = stack.pop()  # remove and return the last item

            if user == user2:
                result = True
                break

            visited.append(user)
            for relationship in user.getPeers():
                nextUser = relationship.getPeer(user)
                if nextUser not in visited:
                    stack.append(nextUser)

        return result

    def getFriends(self, user):
        '''
        return a dict of friends based on tier
        {1:[user, user], 2:[user, user]}
        '''
        if user not in self.userList:
            raise RuntimeError("User does not exist")
        resultDict = {}
        #currentTier = 1
        visited = []
        queue = []

        queue.insert(0, [user, 0])  # insert at index 0, user and current tier

        while len(queue) > 0:
            [user, tier] = queue.pop()  # remove and return the last item
            if user not in visited:
                visited.append(user)
            else:
                continue

            if tier not in resultDict:
                resultDict[tier] = []
            resultDict[tier].append(user)

            for relationship in user.getFriends():
                nextUser = relationship.getPeer(user)
                if nextUser not in visited:
                    queue.insert(0, [nextUser, tier + 1])
        return resultDict

    def getParents(self, user):
        pass

    def getPartners(self, user):
        pass

    def getChilds(self, user):
        pass

    def getFamily(self, user):
        pass
