
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ("rock", "paper", "scissors")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    print(f"You chose {choices['player']} and computer chose {choices['computer']}")
    return choices

def check_win(player, computer):
    if player == computer:
        return "It's a tie"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors, you win!"
    elif player == "rock" and computer == "paper":
        return "Paper covers rock, you lose"
    elif player == "paper" and computer == "scissors":
        return "Scissors slice paper, you lose"
    elif player == "scissors" and computer == "paper":
        return "Scissors cuts paper, you win!"
    elif player == "paper" and computer == "rock":
        return "Paper covers rock, you win"
    elif player == "scissors" and computer == "rock":
        return "Rock smashes scissors, you lose"
    else:
        return "Invalid entry"

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)