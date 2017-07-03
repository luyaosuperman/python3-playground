from dealer import Dealer
from player import Player
from xprint import xPrint, printStack
import xprint

""" 
@startuml
class Game
Game --> Player
Game --> Dealer
Player ..> Dealer
Player --> Cards
Dealer --> Cards
@enduml
"""

"""
@startuml
Game -> Dealer: Create
Game -> Player: Create multiple
Game -> Dealer: SetAsideACard()
Game -> Player: addACard()
loop until all players return true with isPlayerFinished()
Game -> Player: act()
end
@enduml

"""

"""
@startuml
[*] -> Initialized : __initGame()
Initialized -> StartGame
StartGame -> DealerActed 
DealerActed -> PlayerActed
PlayerActed -> GameFished : __judge()
PlayerActed -> StartGame

@enduml
"""


class Game(object):
    """
    Work as Mediator
    Implement the rule of the game
    """

    @printStack
    def __init__(self, numberOfPlayers, numberOfDecks):
        """
        Initiate the Game class
        """
        self.numberOfDecks = numberOfDecks
        self.numberOfPlayers = numberOfPlayers

        self.dealer = None
        self.players = []

        self.gameFinished = False

        self.__initGame()
        self.__game()

    @printStack
    def __game(self):
        """
        Actual logic
        """
        while not self.gameFinished:
            self.__playARound()
            self.__judge()
        self.__finalAction()

    @printStack
    def __createUsers(self):
        """
        Create users
        """
        for i in range(self.numberOfPlayers):
            self.players.append(
                Player(
                    "Player_" + str(i), self.dealer.dealCard
                )
            )

    @printStack
    def __initGame(self):
        """
        Necessary preparation before game can start
        """
        self.dealer = Dealer(self.numberOfDecks)
        self.__createUsers()
        self.dealer.SetAsideACard()
        self.dealer.SetAsideACard()
        self.dealer.revealACard()
        for player in self.players:
            # deal two cards
            player.addACard()
            player.addACard()

    @printStack
    def __playARound(self):
        """
        Let each player run a round

        """
        for player in self.players:
            player.act()

    @printStack
    def __judge(self):
        """
        After each round, 
        check the status of each player
        And end the game if necessary
        """
        for player in self.players:
            if player.isPlayerFinished() == False:
                # short circuit the logic
                return None
        xPrint("all players are finished")
        self.gameFinished = True

    @printStack
    def __finalAction(self):
        """
        Clean up actions before game finishes
        """
        self.dealer.finalAction()
        for player in self.players:
            player.finalAction()
            self.__isPlayerWin(player)

    @printStack
    def __isPlayerWin(self, player):
        """
        check if player wins or loses
        """
        if player.isPlayerSurrendered():
            print("Player %s lost. Surrenderred!" % player.getPlayerName())
            return False

        if self.dealer.getValue() > 21:
            print("Player %s win. Dealer busted!" % player.getPlayerName())
            return True

        if player.getValue() > 21:
            print("Player %s lost on hand 1. Player Busted!" %
                  player.getPlayerName())
        elif player.getValue() >= self.dealer.getValue():
            print("Player %s win on hand 1." % player.getPlayerName())
        else:
            print("Player %s lose on hand 1." % player.getPlayerName())

        if player.isPlayerSplitted():
            print(
                "player %s splitted. Let's look at another hand" %
                player.getPlayerName()
            )

            if player.getValue(2) > 21:
                print("Player %s lost on hand 2. Player Busted!" %
                      player.getPlayerName())
            elif player.getValue(2) >= self.dealer.getValue():
                print("Player %s win on hand 2." % player.getPlayerName())
            else:
                print("Player %s lose on hand 2." % player.getPlayerName())


if __name__ == "__main__":
    game = Game(2, 2)
