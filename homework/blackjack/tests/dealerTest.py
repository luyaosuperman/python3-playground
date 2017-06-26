from dealer import Dealer
from card import Card
import unittest
from unittest.mock import patch
import xprint
from xprint import xPrint


class DealerTest(unittest.TestCase):
    """
    Test out the functionality of class Dealer
    """

    def testInvalidDeck(self):
        """
        Dealer should raise 
        ValueError
        if the numerOfDecks is less than 1
        """
        deck = 0
        self.assertRaises(ValueError, Dealer, deck)

    def __validateDeckCompleteness(self, cards):
        """
        Check if a deck of card contains 52 cards,
        13 for each suit.
        """
        cardsDict = {
            "CLUBS": set(),
            "DIAMONDS": set(),
            "HEARTS": set(),
            "SPADES": set(),
        }
        for card in cards:
            self.assertIn(card.getSuit(), cardsDict)
            self.assertNotIn(card.getRank(), cardsDict[card.getSuit()])
            cardsDict[card.getSuit()].add(card.getRank())
        #xprint.debugPrint = True
        xPrint(cardsDict)

    #@patch('dealer.Dealer._Dealer__shuffleCards', returnValue = 'None')
    def testCreateADeckOfCard(self, *args, **keywargs):
        """
        test if the cards created by dealer is full
        """
        dealer = Dealer(1)
        self.assertEqual(len(dealer.cards), 52)
        self.__validateDeckCompleteness(dealer.cards)

    def testCreateTwoDecksOfCards(self):
        """
        Create 2 decks of cards,
        there should be 104 cards
        """
        dealer = Dealer(2)
        self.assertEqual(len(dealer.cards), 104)

    def testSetAsideACard(self):
        """
        it should set aside a card
        while total number of cards should remain the same
        """
        dealer = Dealer(1)
        dealer.SetAsideACard()
        self.assertEqual(len(dealer.cards), 51)
        self.assertEqual(len(dealer.cardsInGame), 1)
        self.__validateDeckCompleteness(dealer.cards + dealer.cardsInGame)

    def testGetValue(self):
        """
        Dealer.getValue()
        Focus on 'soft' ace, and 11,12,13 -> 10, and their combination
        """

        # 1,3 => 14
        # 1,1 => 12
        # 1,10 => 21
        # 11,11 => 20
        # 13,2 => 12

        testCases = [
            #[rank of card1, rank of card2, corresponding value]
            [1, 3, 14],
            [1, 1, 12],
            [1, 10, 21],
            [11, 11, 20],
            [13, 2, 12],
        ]

        for testCase in testCases:
            rank1, rank2, result = testCase

            """xprint.debugPrint = True
            xPrint(rank1, rank2, result)
            xprint.debugPrint = False"""

            dealer = Dealer(1)
            dealer.cardsInGame = [
                Card("CLUBS", rank1),
                Card("CLUBS", rank2),
            ]
            self.assertEqual(dealer.getValue(), result)

    def testFinalAction(self):
        """
        Make sure dealer will reach "soft" 17
        """

        testCases = [
            #[ [rank of card1, rank of card2], [rank of unused cards, ...], result]
            [[1, 1], [2, 2, 2], 18],  # 12 => 18
        ]
        for testCase in testCases:
            dealer = Dealer(1)

            dealer.cardsInGame = []
            dealer.cards = []

            for rank in testCase[0]:
                dealer.cardsInGame.append(Card("CLUBS", rank))

            for rank in testCase[1]:
                dealer.cards.append(Card("CLUBS", rank))

            dealer.finalAction()
            self.assertEqual(dealer.getValue(), testCase[2])
