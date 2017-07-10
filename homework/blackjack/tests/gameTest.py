import unittest
from unittest.mock import patch
import xprint
from game import Game
from dealer import Dealer
from card import Card


class GameTest(unittest.TestCase):
    """
    Test the function of class Game
    """

    @patch('game.Game._Game__game', return_value=None)
    @patch('game.Game._Game__initGame', return_value=None)
    def setUp(self, *args, **keywargs):
        self.game = Game(2, 2)
        self.game.dealer = Dealer(2)
        self.game._Game__createUsers()
        self.assertEqual(self.game.gameFinished, False)

    def test__judge_GameFinish(self, *args, **keywargs):
        """
        Test if __judge works correctly
        """
        for player in self.game.players:
            player.playerFinished = True
        self.game._Game__judge()
        self.assertEqual(self.game.gameFinished, True)

    def test__judge_GameContinue(self, *args, **keywargs):
        """
        Test if __judge works correctly
        """
        for player in self.game.players:
            player.playerFinished = False
        self.game._Game__judge()
        self.assertEqual(self.game.gameFinished, False)

    def testPlayerWin(self, *args, **keywargs):
        """
        Create a scenario that player will win over dealer
        And check if the game recongnized it correctly.
        """
        self.game.dealer.cardsInGame.append(Card("CLUBS", 10))
        self.game.dealer.cardsInGame.append(Card("CLUBS", 9))

        for player in self.game.players:
            player.cards1.append(Card("CLUBS", 10))
            player.cards1.append(Card("CLUBS", 10))
            self.game._Game__isPlayerWin(player)

            print(player.state1)
            self.assertEqual(player.state1, "WIN")

    def testPlayerLose(self, *args, **keywargs):
        """
        Create a scenario that player will win over dealer
        And check if the game recongnized it correctly.
        """
        self.game.dealer.cardsInGame.append(Card("CLUBS", 10))
        self.game.dealer.cardsInGame.append(Card("CLUBS", 10))

        for player in self.game.players:
            player.cards1.append(Card("CLUBS", 9))
            player.cards1.append(Card("CLUBS", 10))
            self.game._Game__isPlayerWin(player)

            print(player.state1)
            self.assertEqual(player.state1, "LOSE")
