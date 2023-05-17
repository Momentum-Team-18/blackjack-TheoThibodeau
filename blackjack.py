# classes - Deck, Card, Dealer, Player, Game
# create the deck
# shuffle
# add player and dealer
# deal cards
# play hand

import random
# shuffle!

SUITS = ['H', 'S', 'D', 'C']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# all caps is how you write constants in python


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    # this is how you get a more readable version, without
    # this its just a string with random letters and numbers
    # that tells you where the data is stored in memory


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += ' ' + str(card)
        return card

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return 'Dealer'

    def hit(self, card):
        # deal an individual card
        self.hand.append(card)


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

    def choice(self):
        choice = input('Would you like to (h)it or (s)tay? ')
        return


class Game:
    def __init__(self, name):
        self.player = Player(self.get_player_name())
        self.dealer = Dealer()
        self.deck = Deck(suits, ranks)
        self.deck.shuffle()
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.show_cards()

    def get_player_name(self):
        name = input('What is your name?')
        return name

    def deal_card(self, person):
        card = self.deck.cards.pop()
        person.hand.append(card)

    def show_cards(self):
        print(f'{new_game.player} has:')
        for card in self.player.hand:
            print(card)
        print('Dealer has: ')
        for card in self.dealer.hand:
            print(card)

    def player_hand(self):
        choice = self.player.choice()
        if choice == 'h':
            self.deal_card(self.player)


new_game = Game(SUITS, RANKS)
# this is how we instantiate the class - calls the __init__
# method of the class
new_game.player_hand()
new_game.show_cards()
