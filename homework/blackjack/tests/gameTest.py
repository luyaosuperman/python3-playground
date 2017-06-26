import unittest
from unittest.mock import patch
import xprint
from game import Game
from dealer import Dealer


class GameTest(unittest.TestCase):
    """
    Test the function of class Game
    """

    @patch('game.Game._Game__game', return_value=None)
    def test__judge(self, *args, **keywargs):
        """
        Test if __judge works correctly
        """
        game = Game(2, 2)
        game.dealer = Dealer(2)
        game._Game__createUsers()
        self.assertEqual(game.gameFinished, False)
        for player in game.players:
            player.playerFinished = True
        game._Game__judge()
        self.assertEqual(game.gameFinished, True)
