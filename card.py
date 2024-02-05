values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit: str, rank: str):

        """
        The __init__ function is a special function in Python classes. It is run as soon as an object of a class is instantiated.
        The method __init__() is called automatically every time the class is being used to create a new object.

        :param self: Represent the instance of the object itself
        :param suit: str: Define the suit of the card
        :param rank: str: Set the rank of a card
        :return: Nothing
        :doc-author: Trelent
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        """
        The __str__ function is a special function that returns a string representation of an object.
        This is useful for debugging and logging, as it allows you to inspect the contents of an object
        without having to know its type.

        :param self: Refer to the current instance of the class
        :return: The rank and suit of the card
        :doc-author: Trelent
        """
        return f"{self.rank} of {self.suit}"

    def get_value(self):

        """
        The get_value function returns the value of a given node.

        :param self: Represent the instance of the class
        :return: The value of the card
        :doc-author: Trelent
        """
        return self.value
