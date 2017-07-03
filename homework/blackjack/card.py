from xprint import xPrint, printStack


class Card(object):
    """
    Base class of cards
    """

    suits = {
        "CLUBS",
        "DIAMONDS",
        "HEARTS",
        "SPADES",
    }


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
        if self.suit not in Card.suits:
            raise ValueError("the suit provided is not valid")
        if  self.rank < 1 or self.rank > 13:
            raise ValueError("the rank provided is not valid")


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
        return ("%s-%s" % (self.suit, self.rank))
