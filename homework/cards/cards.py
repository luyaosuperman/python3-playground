import random


class Card():
    """
    Base class of cards
    """

    suits = {
        "CLUBS",
        "DIAMONDS",
        "HEARTS",
        "SPADES",
    }

    __usedCombination = set()
    # It should contain the set of cards which is already shuffled,
    # in form of tuple: {(Cards.CLUBS, 1), (Cards.SPADES, 2)}

    def __init__(self, suit, rank):
        """
        Set suit and rank for the card
        And then validate the input
        """
        self.suit = suit
        self.rank = rank
        self.__validateInput()

    def __validateInput(self):
        """
        Validate if the suit and rank makes sense
        Also, make sure no duplicate card will be issued
        """
        assert(self.suit in Card.suits)
        assert(self.rank >= 1 and self.rank <= 13)

        suitRank = (self.suit, self.rank)
        if suitRank in Card.__usedCombination:
            raise RuntimeError(
                "duplicate cards %s %s" % (self.suit, self.rank))
        else:
            Card.__usedCombination.add(suitRank)

    def getSuit(self):
        """
        Get the suit of the card
        """
        return self.suit

    def getRank(self):
        """
        Get the rank of the card
        """
        return self.rank

    def getName(self):
        """
        Get the proper name of the card
        e.g. Clubs Ace, or something else
        """
        return ("%s %s" % (self.suit, self.rank))

#####################################################################


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

#####################################################################


class Referee():
    """
    Manager class, responsible for
    (1) Create and manage users
    (2) Create a deck of cards
    (3) Shuffle cards
    (4) Deal cards
    """

    def __init__(self, numberOfPlayers):
        """
        initate the Referee
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
    referee = Referee(4)
    referee.shuffleCards()
    referee.dealCards()
    for card in referee.cards:
        print(card.getName())
