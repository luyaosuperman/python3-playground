from card import Card
from player import Player
import unittest
import xprint

class PlayerTest(unittest.TestCase):
    """
    Test out the function of class Player
    """

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