class Chips:
    def __init__(self):
        self.total = 5  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def get_total(self):
        return self.total

    def set_bet(self, bet: int) -> bool:
        if bet <= 0:
            print("invalid number!")
            return True
        elif bet <= self.total:
            self.bet = bet
            return False
        else:
            print("This value is above your total!")
            return True
