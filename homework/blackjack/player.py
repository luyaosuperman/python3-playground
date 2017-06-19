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

    def addCard(self, card):
        """
        Add a card to the possession of the user
        """
        self.cards.append(self.funcGetACard())
        self.__checkPlayerFinished()

    def getCards(self):
        """
        Return the cards owned by the player
        """
        return self.cards

    def act(self):
        """
        Set the next action, probablly through console
        And then execute the result
        """
        inputCommand = ""
        while inputCommand.upper() \
                not in self.__getAllowedAction():
            try:
                inputCommand = input("%s : " % self.playerName)
            except Exception, e:
                print(str(e))
        func = self.actionMap[inputCommand.upper()]

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

    def __hit(self, funcGetACard):
        """
        Implement the action "hit"
        """
        cards = self.__getCards()
        card = funcGetACard()
        cards.append(card)
        self.__checkPlayerFinished()

    def __stand(self):
        """
        Implement the action "stand"
        """
        self.stand = 1
        self.playerFinished = True

    def __getCards(self):
        """
        return the correct stack before/after split
        """
        if self.splitHand == 1:
            cards = self.cards1
        else:
            cards = self.cards2
        return cards

    def __checkPlayerFinished(self):
        """
        Check if the player can continue on
        """
        if self.getValue() >= 21:
            self.playerFinished = True

    def isPlayerFinished(self):
        """
        Return if the player is stand
        """
        return self.isPlayerFinished

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
