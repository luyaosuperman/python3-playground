from xprint import xPrint, printStack


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

    # __usedCombination = set()
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
        # If, else, raise

        """suitRank = (self.suit, self.rank)
        if suitRank in Card.__usedCombination:
            raise RuntimeError(
                "duplicate cards %s %s" % (self.suit, self.rank))
        else:
            Card.__usedCombination.add(suitRank)"""

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
