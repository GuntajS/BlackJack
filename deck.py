import random

from card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self):

        """
        The __init__ function is called when the class is instantiated.
        It creates a deck of cards and stores it in an instance variable, self.deck.

        :param self: Refer to the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):

        """
        The __str__ function is a special function that returns a string representation of the object.
        This is useful for debugging and logging purposes, or for use in an interactive Python session.

        :param self: Refer to the object itself
        :return: The string representation of the deck
        :doc-author: Trelent
        """
        deck_str = " "
        for card in self.deck:
            deck_str += f"{str(card)}, "
        return deck_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


if __name__ == '__main__':
    new_deck = Deck()
    print(new_deck)
