from card import Card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += card.get_value()

    def adjust_for_ace(self):
        self.value -= 10

    def __str__(self):
        for card in self.cards:
            print(f"{card}, ")