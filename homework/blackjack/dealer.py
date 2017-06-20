from card import Card
from xprint import xPrint, printStack
import random


class Dealer():
    """
    Manager class, responsible for
    (1) Create and manage users
    (2) Create a deck of cards
    (3) Shuffle cards
    (4) Deal cards
    """

    def __init__(self, numberOfDecks):
        """
        initate the Dealer
        """
        self.numberOfDecks = numberOfDecks

        self.cards = []
        self.usedCards = []

        self.cardsInGame = []  # cards used in game

        self.__createCards()
        self.__shuffleCards()

    @printStack
    def __createCards(self):
        """
        Create a deck of cards
        """
        for deck in range(self.numberOfDecks):
            # Create multiple decks of cards
            for suit in Card.suits:
                for rank in range(1, 13 + 1):
                    self.cards.append(Card(suit, rank))

    @printStack
    def __shuffleCards(self):
        """
        Shuffle cards
        Fisher–Yates shuffle
        https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        """
        for i in range(len(self.cards) - 1):
            j = random.randint(i, len(self.cards) - 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    @printStack
    def dealACard(self):
        """
        Deal a car to a user
        """
        return self.cards.pop()

    @printStack
    def SetAsideACard(self):
        """
        Set aside a card for dealer itself
        """
        self.cardsInGame.append(self.cards.pop())
        self.__showCards()

    def revealACard(self):
        """
        Reveal the last card
        """
        print(
            "One of the dealer's card is",
            self.cardsInGame[-1].getName()
        )

    @printStack
    def act(self):
        """
        Necessary dealer action in a round
        seems to be None?
        """
        pass

    @printStack
    def finalAction(self):
        """
        After every player finishe their move,
        dealer need to do something.
        """
        while self.getValue() < 17:
            self.SetAsideACard()
        print("===============")
        print("dealer's cards:")
        for card in self.cardsInGame:
            print(card.getName())

    @printStack
    def getValue(self):
        """
        return the value of the cards in dealer's hand
        """

        cards = self.cardsInGame
        aceCount = 0
        result = 0
        for card in cards:
            rank = card.getRank()
            if rank == 1:
                aceCount += 2
            elif rank <= 10:
                result += rank
            elif rank <= 13:
                result += 10
            else:
                raise ValueError(
                    "Illegal rank for a card : %s" % rank
                )

        result += aceCount  # ace will be count as at least 1

        # One by one,
        # check if it is good to make ace 10 instaed of 1
        while result + 9 <= 21 and aceCount > 0:
            result += 9
            aceCount -= 1

        xPrint("Dealer's value:", result)
        self.__showCards()

        return result

    def __showCards(self):
        """
        print out all cards
        """
        for card in self.cardsInGame:
            xPrint("cards in dealer:", card.getName())
