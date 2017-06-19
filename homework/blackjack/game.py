from dealer import Dealer


class Game(self):
    """
    Work as Mediator
    Implement the rule of the game
    """

    def __init__(self, numberOfPlayers, numberOfDecks):
        """
        Initiate the Game class
        """
        self.numberOfDecks = self.numberOfDecks
        self.numberOfPlayers = numberOfPlayers

        self.dealer = None
        self.players = []

        self.gameFinished = False

    def __game(self):
        """
        Actual logic
        """
        self.__createUsers()
        self.__initGame()
        while not self.gameFinished:
            self.__playARound()
            self.__judge()
        self.dealer.finalAction()

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

    def __initGame(self):
        """
        Necessary preparation before game can start
        """
        self.dealer = Dealer(self.numberOfDecks)
        self.__createUsers()
        self.dealer.SetAsideACard()
        self.dealer.SetAsideACard()
        for player in self.players:
            # deal two cards
            player.addACard()
            player.addACard()

    def __playARound(self):
        """
        Let each player run a round

        """
        self.dealer.act()
        for player in self.players:
            player.act()

    def __judge(self):
        """
        After each round, 
        check the status of each player
        And end the game if necessary
        """
        for player in self.players:
            if not player.isPlayerFinished:
                return
        self.gameFinished = True
