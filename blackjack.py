# Write your blackjack game here.
# classes include: Deck | Card | Dealer | Player | Game
# create the Deck
# shuffle the Deck
# add Player & Dealer
# deal cards
# play Game

import random

SUITS = ['♥︎', '♠︎', '♣︎', '♦︎']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)
                # deck_of_cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += ' ' + str(card)
        return deck_string

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return 'Dealer'
    
    def hit(self, card):
        self.hand.append(card)


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

    def choice(self):
        choice = input("Would you like to (h)it or (s)tay: ")
        return choice


class Game:
    def __init__(self, suits, ranks):
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
        name = input('What is your name? ')
        return name

    def deal_card(self, person):
        card = self.deck.cards.pop()
        person.hand.append(card)

    def show_cards(self):
        print(f'{self.player} has: ')
        for card in self.player.hand:
            print(card)
        print('Dealer has: ')
        for card in self.dealer.hand:
            print(card)

    def player_hand(self):
        choice = self.player.choice()
        if choice == 'h':
            self.deal_card(self.player)
        
    def player_card_values(self):
        player_sum = []
        for card in self.player.hand:
            if card.rank in range(2, 10):
                player_sum.append(card.rank)
            if card.rank == 'J':
                player_sum.append(10)
            if card.rank == 'Q':
                player_sum.append(10)
            if card.rank == 'K':
                player_sum.append(10)
            if card.rank == 'A':
                if sum(player_sum) >= 11:
                    player_sum.append(1)
                if sum(player_sum) <= 10:
                    player_sum.append(11)
        self.player_total = sum(player_sum)
        if sum(player_sum) == 21:
            print(f'{self.player} Wins!')
        elif sum(player_sum) > 21:
            print(f'{self.player} Loses!')
        print(f"{self.player} has a score of {self.player_total}")
        return sum(player_sum)
        
    def dealer_card_values(self):
        dealer_sum = []
        for card in self.dealer.hand:
            if card.rank in range(2, 10):
                dealer_sum.append(card.rank)
            if card.rank == 'J':
                dealer_sum.append(10)
            if card.rank == 'Q':
                dealer_sum.append(10)
            if card.rank == 'K':
                dealer_sum.append(10)
            if card.rank == 'A':
                if sum(dealer_sum) >= 11:
                    dealer_sum.append(1)
                if sum(dealer_sum) <= 10:
                    dealer_sum.append(11)
        self.dealer_total = sum(dealer_sum)

        if sum(dealer_sum) < 17:
            self.deal_card(self.dealer)
        elif sum(dealer_sum) == 21:
            print('Dealer Wins!')
        elif sum(dealer_sum) > 21:
            print(f'{self.player} Wins!')
        
        print(f"{self.dealer} has a score of {self.dealer_total}")
        return sum(dealer_sum)

new_game = Game(SUITS, RANKS)
new_game.player_hand()
new_game.player_card_values()
new_game.dealer_card_values()
new_game.show_cards()
# for card in new_game.player.hand:
#     print(card)
    # def game_rules(self): 
    #     player_score = self.player_card_values()
    #     if sum(dealer_sum) < 17:
    #         self.deal_card(self.dealer)
    #     if sum(dealer_sum) == sum(player_sum) :
    #         print('Dealer Wins!')
    #     elif 
            
    #     if sum(dealer_sum) > 21:
    #         print(f'{self.player} Wins!')
    #     self.dealer_total = sum(dealer_sum)