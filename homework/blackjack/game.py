from dealer import Dealer
from player import Player
from xprint import xPrint, printStack

class Game():
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

        self.__game()

    @printStack
    def __game(self):
        """
        Actual logic
        """
        self.__initGame()
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
                    "Player_" + str(i), self.dealer.dealACard
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
        self.dealer.act()
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
                return
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
            if self.__isPlayerWin(player):
                print("++ player %s win!" % player.playerName)
            else:
                print("-- player %s lose!" % player.playerName)

    @printStack
    def __isPlayerWin(self, player):
        """
        check if player wins or loses
        """
        if self.dealer.getValue() > 21:
            return True

        if player.getValue() > 21:
            return False

        if player.getValue() >= self.dealer.getValue():
            return True


if __name__ == "__main__":
    game = Game(1, 1)
