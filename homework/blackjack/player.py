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

    STATE = {
        "NA",
        "PENDING",
        "WIN",
        "LOSE",
        "SURRENDER"
    }

    def __init__(self, playerName, dealer):
        """
        set the name of player, for identification purpose
        """
        self.playerName = playerName
        self.dealer = dealer  # Dealer.dealACard()
        self.cards1 = []  # used by default
        self.cards2 = []  # becoume useful after split

        self.state1 = "PENDING"
        self.state2 = "NA"

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
    def addCard(self):
        """
        Add a card to the possession of the user
        """
        cards = self.__getCards()
        cards.append(self.dealer.dealCard())
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
        self.__checkPlayerFinished()
        if not self.playerFinished:
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
        else:
            print("player %s finished!" % self.playerName)

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
        cards.append(self.dealer.dealCard())
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
        self.cards1.append(self.dealer.dealCard())
        self.cards2.append(self.dealer.dealCard())
        self.state2 = "PENDING"
        self.playerFinished = True

    def __double(self):
        """
        Implement the action "double"
        """
        print("player %s DOUBLE!" % self.playerName)
        cards = self.__getCards()
        cards.append(self.dealer.dealCard())
        self.doubled = True
        self.playerFinished = True

    def __surrender(self):
        """
        Implement the action "surrender"
        """
        print("player %s SURRENDER!" % self.playerName)
        self.surrendered = True
        self.state1 = "LOSE"
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
        if self.getValue(1) >= 21:
            print("player %s busted!" % self.playerName)
            self.playerFinished = True
            self.state1 = "lose"

        if self.getValue(2) >= 21:
            print("player %s busted!" % self.playerName)
            self.playerFinished = True
            self.state2 = "lose"

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

    def setState(self, state, hand=1):
        """
        this is the func which Game class will use to set
        the state of player, after comparing with Dealer
        """
        if state not in Player.STATE:
            raise RuntimeError("invalid state: %s" % state)

        if hand == 1:
            self.state1 = state
        elif hand == 2:
            self.state2 = state
        else:
            raise ValueError("invalid hand: %s" % hand)
