def test_winner():
    assert determine_winner("rock", "rock") == "TIE GAME"
    assert determine_winner("paper", "paper") == "TIE GAME"
    assert determine_winner("scissors", "scissors") == "TIE GAME"

    assert determine_winner("rock", "paper") == "COMP WINS"
    assert determine_winner("paper", "rock") == "PLAYER WINS"
    assert determine_winner("rock", "scissors") == "PLAYER WINS"
    assert determine_winner("scissors", "paper") == "PLAYER WINS"
    assert determine_winner("paper", "scissors") == "COMP WINS"
    assert determine_winner("scissors", "rock") == "COMP WINS"
    assert determine_winner("paper", "scissors") == "COMP WINS"
    assert determine_winner("scissors", "rock") == "COMP WINS"
    assert determine_winner("rock", "paper") == "COMP WINS"
import random

def test_random_winner():
    choices = ["rock", "paper", "scissors"]
    for _ in range(100):
        player = random.choice(choices)
        computer = random.choice(choices)
        result = determine_winner(player, computer)
        assert result in ["TIE GAME", "PLAYER WINS", "COMP WINS"]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "TIE GAME"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "PLAYER WINS"
    else:
        return "COMP WINS"
# Rock Paper Scissors Game Tests
def test_rps_game():
    print("Welcome to my game!")
    player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ").strip().lower()
    print("user chose", player_choice)

    VALID_CHOICES = {'rock', 'paper', 'scissors'}
    if player_choice not in VALID_CHOICES:
        raise ValueError("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")

    computer_choice = random.choice(list(VALID_CHOICES))
    print("computer chose", computer_choice)

    result = determine_winner(player_choice, computer_choice)
    print("WINNER:", result)
    # Here we would normally assert the expected outcome based on player_choice and computer_choice