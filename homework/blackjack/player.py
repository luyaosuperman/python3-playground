class Player():
    """
    Player class who holds the cards after the deal
    """

    def __init__(self, playerName):
        """
        set the name of player, for identification purpose
        """
        self.playerName = playerName
        self.cards = []

    def addCard(self, card):
        """
        Add a card to the possession of the user
        """
        self.cards.append(card)

    def getCards(self):
        """
        Return the cards owned by the player
        """
        return self.cards