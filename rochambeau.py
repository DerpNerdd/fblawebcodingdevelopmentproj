import random

class RockPaperScissorsGame:
    def __init__(self):
        self.player = Player()
        self.computer_score = 0

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        if (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or (player_choice == "Scissors" and computer_choice == "Paper")
            or (player_choice == "Paper" and computer_choice == "rock")
        ):
            self.player.increase_score()
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_round(self):
        player_choice = self.player.get_choice()
        computer_choice = self.get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        result = self.determine_winner(player_choice, computer_choice)
        print(result)
        print(f"||| Your Score: {self.player.get_score()} ||| Computer Score: {self.computer_score} |||")

    def get_computer_choice(self):
        return random.choice(["Rock", "Paper", "Scissors"])

    def play(self):
        print("Rules:")
        print("Rock beats Scissors (Woah)")
        print("Scissors beats Paper (Amazing)")
        print("Paper beats Rock (Insane in the membrane)")
        print("If you tie you tie :D")
        print("Glhf")
        while True:
            self.play_round()
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again == "no":
                print("Thanks for playing!")
                break

class Player:
    def __init__(self):
        self.score = 0

    def get_choice(self):
        while True:
            player_choice = input("Enter your choice (Rock, Paper, or Scissors): ")
            if player_choice in ["Rock", "Paper", "Scissors"]:
                return player_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
