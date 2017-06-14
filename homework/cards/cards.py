
class Cards():
    """
    Base class of cards
    """

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    __usedCombination = set()
    # It should contain the set of cards which is already shuffled, 
    # in form of tuple: {(Cards.CLUBS, 1), (Cards.SPADES, 2)}

    def __validateInput(self, suit, rank):
    """
    Validate if the suit and rank makes sense
    Also, make sure no duplicate card will be issued
    """

    def __init__(self, suit, rank):

    def setSuit(self):
    """
    Set the suit of the card
    """

    def getSuit(self):
    """
    Get the suit of the card
    """
   
    def setRank(self):
    """
    Set the rank of the card
    """

    def getRank(self):
    """
    Get the rank of the card
    """

    def getName(self):
    """
    Get the proper name of the card
    e.g. Clubs Ace, or something else
    """

#####################################################################
class Player():
    """
    Player class who holds the cards after the deal
    """

    def __init__(self, playerName):
    """
    set the name of player, for identification purpose
    """

    def addCard(self, card):
    """
    Add a card to the possession of the user
    """

    def getCards(self):
    """
    Return the cards owned by the player
    """

#####################################################################
class Referee():
    """
    Manager class, responsible for
    (1) Create and manage users
    (2) Create a deck of cards
    (3) Shuffle cards
    (4) Deal cards
    """
    
    def __init__(self, numberOfPlayers):
    """
    initate the Referee
    """

    def __createUsers(self):
    """
    Create users
    """

    def __createCards(self):
    """
    Create a deck of cards
    """

