from xprint import xPrint, printStack
from card import Card


class Player(object):
    """
    Player class who holds the cards after the deal
    """

    ACTIONS = {
        "HIT",
        "STAND",
        "DOUBLE"
        "SPLIT",
        "SURRENDER"
    }

    def __init__(self, playerName, funcGetACard):
        """
        set the name of player, for identification purpose
        """
        self.playerName = playerName
        self.funcGetACard = funcGetACard  # Dealer.dealACard()
        self.cards1 = []  # used by default
        self.cards2 = []  # becoume useful after split

        self.playerFinished = False
        self.stand = False
        self.surrendered = False
        self.doubled = False
        self.splitted = False

        self.actionMap = {
            "HIT": self.__hit,
            "STAND": self.__stand,
            "DOUBLE": self.__double,
            "SPLIT": self.__split,
            "SURRENDER": self.__surrender,
        }

    @printStack
    def addACard(self):
        """
        Add a card to the possession of the user
        """
        cards = self.__getCards()
        cards.append(self.funcGetACard())
        self.__checkPlayerFinished()
        self.__showCards()

    @printStack
    def getCards(self):
        """
        Return the cards owned by the player
        """
        return self.__getCards()

    @printStack
    def act(self):
        """
        Set the next action, probablly through console
        And then execute the result
        """
        print("player %s's cards:" % self.playerName)
        for card in self.__getCards():
            print(card.getName())
        inputCommand = ""
        allowedCommands = self.__getAllowedAction()
        for allowedCommand in allowedCommands:
            print("player %s is allowed to: %s" %
                  (self.playerName, allowedCommand)
                  )
        while inputCommand.upper() \
                not in allowedCommands:
            try:
                inputCommand = self.__getUserInput(
                    "%s : " % self.playerName
                )
            except Exception as e:
                print(str(e))
        func = self.actionMap[inputCommand.upper()]
        func()

    @printStack
    def __getAllowedAction(self):
        """
        After implementing chips, it is necessary to
        return the list of allowed actions based on chips
        """

        # Without implementing chips, evey action is allowed
        allowedCommands = {
            "HIT",
            "STAND",
            "DOUBLE",
            "SURRENDER",
        }
        if self.cards1[0].getRank() == self.cards1[1].getRank():
            allowedCommands.add("SPLIT")

        # DEBUG ONLY!
        # allowedCommands.add("SPLIT")
        return allowedCommands

    @printStack
    def __getUserInput(self, prompt):
        return input(prompt)

    @printStack
    def __hit(self):
        """
        Implement the action "hit"
        """
        print("player %s HIT!" % self.playerName)
        cards = self.__getCards()
        cards.append(self.funcGetACard())
        # other actions will stop the play.
        # only hit allows player to contine on with other options.
        self.__checkPlayerFinished()

    @printStack
    def __stand(self):
        """
        Implement the action "stand"
        """
        print("player %s STAND!" % self.playerName)
        self.stand = True
        self.playerFinished = True

    @printStack
    def __split(self):
        """
        Implement the action "split"
        """
        print("player %s SPLIT!" % self.playerName)
        self.splitted = True
        self.cards2.append(self.cards1.pop())  # pop last item
        self.cards1.append(self.funcGetACard())
        self.cards2.append(self.funcGetACard())
        self.playerFinished = True

    def __double(self):
        """
        Implement the action "double"
        """
        print("player %s DOUBLE!" % self.playerName)
        cards = self.__getCards()
        cards.append(self.funcGetACard())
        self.doubled = True
        self.playerFinished = True

    def __surrender(self):
        """
        Implement the action "surrender"
        """
        print("player %s SURRENDER!" % self.playerName)
        self.surrendered = True
        self.playerFinished = True

    @printStack
    def __getCards(self, hands=1):
        """
        return the correct stack before/after split
        """
        if hands == 1:
            cards = self.cards1
        else:
            cards = self.cards2
        return cards

    @printStack
    def __checkPlayerFinished(self):
        """
        Check if the player can continue on
        """
        if self.getValue() >= 21:
            print("player %s busted!" % self.playerName)
            self.playerFinished = True

    @printStack
    def isPlayerFinished(self):
        """
        Return if the player is stand
        """
        return self.playerFinished

    @printStack
    def isPlayerSplitted(self):
        """
        Return if the player is splitted
        """
        return self.splitted

    def isPlayerSurrendered(self):
        """
        Return if the player surrenedered
        """
        return self.surrendered

    @printStack
    def getValue(self, hands=1):
        """
        get the value of cards in player's hand
        """

        cards = self.__getCards(hands)
        aceCount = 0
        result = 0
        for card in cards:
            rank = card.getRank()
            if rank == 1:
                aceCount += 1
            elif rank <= 10:
                result += rank
            elif rank <= 13:
                result += 10
            else:
                raise ValueError(
                    "Illegal rank for a card : %s" % rank
                )

        result += aceCount  # ace will be count as at least 1

        # One by one,
        # check if it is good to make ace 10 instaed of 1
        while result + 10 <= 21 and aceCount > 0:
            result += 10
            aceCount -= 1

        xPrint("Player %s's value:" % self.playerName, result)
        self.__showCards()

        return result

    @printStack
    def __showCards(self):
        """
        print out all cards
        """
        cards = self.__getCards()
        for card in cards:
            xPrint(
                "cards in player %s:" % self.playerName,
                card.getName()
            )

    @printStack
    def getPlayerName(self):
        """
        return playerName
        """
        return self.playerName

    @printStack
    def finalAction(self):
        """
        final clean up action of a player
        """

        print("---------------")
        print("player %s's cards in hand1:" % self.playerName)
        for card in self.__getCards():
            print(card.getName())

        # if splitted, print another hand of cards
        if self.splitted == True:
            print("player %s's cards in hand2:" % self.playerName)
            for card in self.cards2:
                print(card.getName())
