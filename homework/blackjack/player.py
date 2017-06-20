from xprint import xPrint, printStack
from card import Card


class Player():
    """
    Player class who holds the cards after the deal
    """

    ACTIONS = {
        "HIT",
        "STAND",
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
        self.busted = False
        self.splitted = None
        self.splitHand = 1
        # After the split, whether the player will choose
        # hand 1 or hand 2

        self.actionMap = {
            "HIT": self.__hit,
            "STAND": self.__stand,
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
                inputCommand = input("%s : " % self.playerName)
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
        return {
            "HIT",
            "STAND",
        }

    @printStack
    def __hit(self):
        """
        Implement the action "hit"
        """
        xPrint("player %s HIT!" % self.playerName)
        cards = self.__getCards()
        card = self.funcGetACard()
        cards.append(card)
        self.__checkPlayerFinished()

    @printStack
    def __stand(self):
        """
        Implement the action "stand"
        """
        xPrint("player %s STAND!" % self.playerName)
        self.stand = 1
        self.playerFinished = True

    @printStack
    def __getCards(self):
        """
        return the correct stack before/after split
        """
        if self.splitHand == 1:
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
            xPrint("player %s busted!" % self.playerName)
            self.playerFinished = True

    @printStack
    def isPlayerFinished(self):
        """
        Return if the player is stand
        """
        return self.isPlayerFinished

    @printStack
    def getValue(self):
        """
        get the value of cards in player's hand
        """

        cards = self.__getCards()
        aceCount = 0
        result = 0
        for card in cards:
            rank = card.getRank()
            if rank == 1:
                aceCount += 2
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
        while result + 9 <= 21 and aceCount > 0:
            result += 9
            aceCount -= 1

        xPrint("Player %s's value:" % self.playerName, result)
        self.__showCards()

        return result

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
    def finalAction(self):
        """
        final clean up action of a player
        """

        print("---------------")
        print("player %s's cards:" % self.playerName)
        for card in self.__getCards():
            print(card.getName())
