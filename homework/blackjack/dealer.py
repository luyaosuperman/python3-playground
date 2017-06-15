class Dealer():
    """
    Manager class, responsible for
    (1) Create and manage users
    (2) Create a deck of cards
    (3) Shuffle cards
    (4) Deal cards
    """

    def __init__(self, numberOfPlayers):
        """
        initate the Dealer
        """
        assert(
            numberOfPlayers > 0
            and numberOfPlayers < 52
            and 52 % numberOfPlayers == 0
        )
        self.players = []
        self.numberOfPlayers = numberOfPlayers

        self.cards = []

        self.__createUsers()
        self.__createCards()

    def __createUsers(self):
        """
        Create users
        """
        for i in range(self.numberOfPlayers):
            self.players.append(Player("Player_" + str(i)))

    def __createCards(self):
        """
        Create a deck of cards
        """
        for suit in Card.suits:
            for rank in range(1, 13 + 1):
                self.cards.append(Card(suit, rank))

    def shuffleCards(self):
        """
        Shuffle cards
        Fisher–Yates shuffle
        https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        """
        for i in range(len(self.cards) - 1):
            j = random.randint(i, len(self.cards) - 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def __validateCardsIntegrity(self, cards=None):
        """
        Validates that all 52 cards are still there, especially after shuffle
        """
        cardDict = {
            "CLUBS": set(),
            "DIAMONDS": set(),
            "HEARTS": set(),
            "SPADES": set(),
        }
        if cards == None:
            cards = self.cards
        for card in cards:
            cardDict[card.getSuit()].add(card.getRank())

        for suit in cardDict:
            assert(len(cardDict[suit]) == 13)

    def dealCards(self):
        """
        Deal cards to players
        """
        for i in range(len(self.cards)):
            self.players[i % len(self.players)].addCard(self.cards[i])

        # Last card should go to last player
        assert(
            i % (len(self.players)) == len(self.players) - 1
        )

    def __validateDeal(self):
        cards = []
        for player in self.players:
            cards += self.players.getCards()
        self.__validateCardsIntegrity(cards=cards)

if __name__ == "__main__":
    dealer = Dealer(4)
    dealer.shuffleCards()
    dealer.dealCards()
    for card in dealer.cards:
        print(card.getName())
