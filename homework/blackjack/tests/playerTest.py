from card import Card
from player import Player
import unittest
from unittest.mock import patch
import xprint


class PlayerTest(unittest.TestCase):
    """
    Test out the function of class Player
    """

    def setUp(self):
        ranks = [2, 3, 4, 5, 6]
        self.cards = []
        for rank in ranks:
            self.cards.append(Card("CLUBS", rank))

    def test__init__(self):
        """
        Test if __init__ is correct
        """
        player = Player("Player_0", self)
        self.assertEqual(len(player.cards1), 0)
        self.assertEqual(player.playerFinished, False)
        self.assertEqual(player.stand, False)
        self.assertEqual(player.surrendered, False)
        self.assertEqual(player.doubled, False)
        self.assertEqual(player.splitted, False)

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

            player = Player("", None)
            player.cards1 = [
                Card("CLUBS", rank1),
                Card("CLUBS", rank2),
            ]
            self.assertEqual(player.getValue(), result)

    def dealCard(self):
        """
        The function to be passed to the class Player
        It should provide a card on request
        """
        return self.cards.pop(0)

    @patch('player.Player._Player__getUserInput', return_value='hit')
    def testHit(self, *args, **keywargs):
        """
        Make sure hit is working as expected
        """
        player = Player("Player_0", self)
        player.addCard()  # 2
        player.addCard()  # 3
        player.act()
        self.assertEqual(len(player.cards1), 3)
        self.assertEqual(player.cards1[2].getRank(), 4)
        self.assertEqual(player.playerFinished, False)
        self.assertEqual(player.stand, False)
        self.assertEqual(player.surrendered, False)
        self.assertEqual(player.doubled, False)
        self.assertEqual(player.splitted, False)

    @patch('player.Player._Player__getUserInput', return_value='hit')
    def test__checkPlayerFinished(self, *args, **keywargs):
        """
        Test if player can detect busted player after hit
        """
        player = Player("Player_0", self)
        player.cards1 = [Card("CLUBS", 10), Card("CLUBS", 11)]
        player.act()
        self.assertEqual(len(player.cards1), 3)
        self.assertEqual(player.cards1[2].getRank(), 2)
        self.assertEqual(player.playerFinished, True)
        self.assertEqual(player.stand, False)
        self.assertEqual(player.surrendered, False)
        self.assertEqual(player.doubled, False)
        self.assertEqual(player.splitted, False)

    @patch('player.Player._Player__getUserInput', return_value='stand')
    def testStand(self, *args, **keywargs):
        """
        Make sure hit is working as expected
        """
        player = Player("Player_0", self)
        player.addCard()  # 2
        player.addCard()  # 3
        player.act()
        self.assertEqual(len(player.cards1), 2)
        self.assertEqual(player.cards1[1].getRank(), 3)
        self.assertEqual(player.playerFinished, True)
        self.assertEqual(player.stand, True)
        self.assertEqual(player.surrendered, False)
        self.assertEqual(player.doubled, False)
        self.assertEqual(player.splitted, False)

    @patch('player.Player._Player__getUserInput', return_value='split')
    @patch(
        'player.Player._Player__getAllowedAction',
        return_value={
            "HIT",
            "STAND",
            "DOUBLE",
            "SURRENDER",
            "SPLIT",
        }
    )
    def testSplit(self, *args, **keywargs):
        """
        Make sure split is working as expected
        """
        player = Player("Player_0", self)
        player.addCard()  # 2
        player.addCard()  # 3
        player.act()
        self.assertEqual(len(player.cards1), 2)
        self.assertEqual(len(player.cards1), 2)
        self.assertEqual(player.cards1[1].getRank(), 4)
        self.assertEqual(player.cards2[1].getRank(), 5)
        self.assertEqual(player.playerFinished, True)
        self.assertEqual(player.stand, False)
        self.assertEqual(player.surrendered, False)
        self.assertEqual(player.doubled, False)
        self.assertEqual(player.splitted, True)

    @patch('player.Player._Player__getUserInput', return_value='double')
    def testDouble(self, *args, **keywargs):
        """
        Make sure double is working as expected
        """
        player = Player("Player_0", self)
        player.addCard()  # 2
        player.addCard()  # 3
        player.act()
        self.assertEqual(len(player.cards1), 3)
        self.assertEqual(player.cards1[2].getRank(), 4)
        self.assertEqual(player.playerFinished, True)
        self.assertEqual(player.stand, False)
        self.assertEqual(player.surrendered, False)
        self.assertEqual(player.doubled, True)
        self.assertEqual(player.splitted, False)

    @patch('player.Player._Player__getUserInput', return_value='surrender')
    def testSurrender(self, *args, **keywargs):
        """
        Make sure surrender is working as expected
        """
        player = Player("Player_0", self)
        player.addCard()  # 2
        player.addCard()  # 3
        player.act()
        self.assertEqual(len(player.cards1), 2)
        self.assertEqual(player.cards1[1].getRank(), 3)
        self.assertEqual(player.playerFinished, True)
        self.assertEqual(player.stand, False)
        self.assertEqual(player.surrendered, True)
        self.assertEqual(player.doubled, False)
        self.assertEqual(player.splitted, False)
