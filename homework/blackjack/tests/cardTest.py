from card import Card
import unittest
import xprint


class CardTest(unittest.TestCase):
    """
    Test out the functionality of clss Card
    """

    def testGetCardProperty(self):
        """
        Build a new card, 
        and then check if the card returns the correct property
        """
        for suit in Card.suits:
            for rank in range(1, 13 + 1):
                card = Card(suit, rank)
                self.assertEqual(suit, card.getSuit())
                self.assertEqual(rank, card.getRank())

    def testInvalidSuit(self):
        """
        Card class should throw 
        ValueError("the suit provided is not valid")
        if the suit provided is not valid
        """
        suit = "errorerror"
        rank = 1
        self.assertRaises(ValueError, Card, suit, 1)

    def testInvalidRank_TooSmall(self):
        """
        Card class should throw
        ValueError
        if the rank provided is not valid
        """
        suit = "CLUBS"
        rank = 0
        self.assertRaises(ValueError, Card, suit, rank)

    def testInvalidRank_TooLarge(self):
        """
        Card class should throw
        ValueError
        if the rank provided is not valid
        """
        suit = "CLUBS"
        rank = 14
        self.assertRaises(ValueError, Card, suit, rank)
