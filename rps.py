import random

ACTIONS = ['Rock', 'Paper', 'Scissors']


class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def __str__(self):
        return f"Hello, {self.name}. Let's play RPS"


class Computer:
    def __init__(self):
        self.choice = None


class PlayGame:
    def __init__(self):
        self.player = Player(self.get_player_name())
        self.computer = Computer()

    def get_player_name(self):
        name = input("What is your name? ")
        return name

    def pick_option(self):
        pick_option = input("Please pick: rock, paper or scissors: ")
        print(f'You chose {pick_option}')
        self.player.choice = pick_option

    def computer_choice(self):
        computer_choice = random.choice(ACTIONS)
        print(f'Computer chose {computer_choice}')
        self.computer.choice = computer_choice

    def check_winner(self):
        if self.computer.choice == self.player.choice:
            print("It's a tie.")
        elif self.player.choice == "rock":
            if self.computer.choice == "scissors":
                print("Rock smashes paper! You win!")
            else:
                print("Paper covers rock. You lose.")
        elif self.player.choice == "paper":
            if self.computer.choice == "rock":
                print("Paper covers rock. You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif self.player.choice == "scissors":
            if self.computer.choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")


play_again = True
while play_again:
    new_game = PlayGame()
    new_game.pick_option()
    new_game.computer_choice()
    new_game.check_winner()

    play = input("would you like to play again (y/n)")
    if play == ('n'):
        print("thanks for playing")
        break
    elif play == ('y'):
        new_game.pick_option()
        new_game.computer_choice()
        new_game.check_winner()