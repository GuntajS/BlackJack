from chips import Chips
from deck import Deck
from hand import Hand
from player import Player


global playing
playing = True


def take_bet(chips: Chips):

    """
    The take_bet function takes in the player's chips as an argument and prompts them to enter their bet.
        It then checks that the bet is valid, and if it isn't, asks for a new one.

    :param chips: Chips: Pass in the chips object and to allow
    :return: Nothing

    """
    unconfirmed_bet = True
    while unconfirmed_bet:
        try:
            bet = int(input("Please enter the amount you would like to bet: "))
            unconfirmed_bet = chips.set_bet(bet)
        except ValueError and TypeError:
            print("This is not an int, please try again")


def hit(deck: Deck, hand: Hand):

    """
    The hit function takes in a deck and hand, deals a card from the deck to the hand,
    and adjusts for an ace if necessary. It returns nothing.

    :param deck: Deck: Pass in the deck object to the function
    :param hand: Hand: Add a card to the hand
    :return: Nothing, but it does modify the hand
    :doc-author: Trelent
    """
    temp = deck.deal()
    if temp.rank == 'Ace' and hand.value > 10:
        hand.adjust_for_ace()
        hand.add_card(temp)
    else:
        hand.add_card(temp)


def hit_or_stand(deck: Deck, hand: Hand):

    """
    The hit_or_stand function prompts the player to hit or stand and then returns a boolean value
        True if the player has chosen to stand, False otherwise.

        Args:
            deck (Deck): The deck of cards from which cards are drawn.  This is passed by reference so that it can be modified in place.

    :param deck: Deck: Pass the deck to the function
    :param hand: Hand: Pass the hand object to the function
    :return: The value of the playing variable
    :doc-author: Trelent
    """
    print(f"1) Hit\nor\n2) Stand")
    choice = int(input())
    match choice:
        case 1:
            hit(deck, hand)
            return True
        case 2:
            return False


def show_some(player: Player, dealer: Player):

    """
    The show_some function is used to display the player's hand and one of the dealer's cards.
    This function takes two arguments: a Player object representing the player, and a Player object
    representing the dealer.

    :param player: Player: Pass the player object to the function
    :param dealer: Player: Display the dealers first card
    :return: The player's and dealer's cards

    """
    print("Player:\n")
    for card in player.hand.cards:
        print(card)
    print(f"Dealer:\n{dealer.hand.cards[0]}")


def show_all(player: Player, dealer: Player):



    """
    The show_all function prints the player's and dealer's hands, as well as their values.
        Args:
            player (Player): The Player object.
            dealer (Dealer): The Dealer object.

    :param player: Player: Pass the player object into the function
    :param dealer: Player: Pass the dealer object into the function
    :return: The value of the player and dealer hands

    """
    print("Player:\n")
    for card in player.hand.cards:
        print(card)
    print(f"Player Value: {player.hand.value}\n")
    print("Dealer:\n")
    for card in dealer.hand.cards:
        print(card)
    print(f"Dealer Value: {dealer.hand.value}")


def player_busts(player):

    """
    The player_busts function will be called when the player's hand exceeds 21.
        It will inform the player of their loss, and deduct the bet amount from their chips.

    :param player: Determine if the player has busted
    :return: The player's chips
    :doc-author: Trelent
    """
    player.chips.lose_bet()
    print("dealer has won")


def player_wins(player: Player):

    """
    The player_wins function takes in a player object and adds the bet amount to the players chips.
        Args:
            player (Player): The Player object that is passed into this function.

    :param player: Player: Pass the player object into the function
    :return: Nothing
    :doc-author: Trelent
    """
    player.chips.win_bet()
    print("player has won")


def dealer_busts(player: Player):

    """
    The dealer_busts function will be called when the dealer's hand exceeds 21.
        It awards the player a win and prints out an appropriate message.

    :param player: Player: Pass the player object into the function
    :return: Nothing
    :doc-author: Trelent
    """
    player.chips.win_bet()
    print("player has won")


def dealer_wins(player: Player):

    """
    The dealer_wins function takes in a player object and subtracts the bet amount from the players chips.
        It then prints out that the dealer has won.

    :param player: Player: Pass the player object to the function
    :return: A string
    :doc-author: Trelent
    """
    player.chips.lose_bet()
    print("dealer has won")




def main():

    """
    The main function is the entry point of the program.
    It initializes a deck, shuffles it and deals two cards to each player.
    Then it prompts for a bet from the player and shows some cards (but keeps one dealer card hidden).
    After that, if playing is True (which means that hit_or_stand() returned True),
    the function asks for another hit or stand from the player until he busts or stands.
    If he busts, then dealer wins; otherwise, if his hand value exceeds 21 then dealer wins;
    otherwise if his hand value is greater than dealers' then he

    :return: A value
    :doc-author: Trelent
    """
    while True:
        # Print an opening statement
        print("Welcome to BlackJack!")

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        player = Player(Hand(), Chips())
        dealer = Player(Hand(), Chips())
        player.set_cards(deck.deal())
        dealer.set_cards(deck.deal())
        player.set_cards(deck.deal())
        dealer.set_cards(deck.deal())

        # Prompt the Player for their bet
        take_bet(player.chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            a = True
            while a or player.hand.value>21 :
                a = hit_or_stand(deck, player.hand)
                show_some(player, dealer)



            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.hand.value > 21:
                player_busts(player)
                break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            while dealer.hand.value < 17:
                hit(deck, dealer.hand)

            # Show all cards
            show_all(player, dealer)
            # Run different winning scenarios
            if dealer.hand.value > 21:
                dealer_busts(player)
            elif dealer.hand.value > player.hand.value:
                dealer_wins(player)
            else:
                player_wins(player)

            # Inform Player of their chips total
            print(f"Your chips total are: {player.chips.get_total()}")
            break

            # Ask to play again
            # if input("Do you want to play again? ").lower() == 'yes':
            #     pass
            # else:
            #     break


if __name__ == '__main__':
    main()
