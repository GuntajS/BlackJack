from card import Card
from chips import Chips
from hand import Hand


class Player:

    def __init__(self, hand: Hand, chips: Chips):
        self.hand = hand
        self.chips = chips

    def set_cards(self, card: Card):
        self.hand.add_card(card)
