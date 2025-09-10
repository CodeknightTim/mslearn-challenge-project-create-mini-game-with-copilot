# Rock-Paper-Scissors Minigame
import random

def get_computer_choice():
	return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
	while True:
		choice = input("Enter rock, paper, or scissors: ").strip().lower()
		if choice in ["rock", "paper", "scissors"]:
			return choice
		else:
			print("Invalid option. Please choose rock, paper, or scissors.")

def determine_winner(player, computer):
	if player == computer:
		return "tie"
	elif (
		(player == "rock" and computer == "scissors") or
		(player == "scissors" and computer == "paper") or
		(player == "paper" and computer == "rock")
	):
		return "win"
	else:
		return "lose"

def play_game():
	score = 0
	rounds = 0
	while True:
		player = get_player_choice()
		computer = get_computer_choice()
		print(f"Computer chose: {computer}")
		result = determine_winner(player, computer)
		if result == "win":
			print("You win!")
			score += 1
		elif result == "lose":
			print("You lose!")
		else:
			print("It's a tie!")
		rounds += 1
		again = input("Play again? (y/n): ").strip().lower()
		if again != "y":
			break
	print(f"\nGame over! You won {score} out of {rounds} rounds.")

if __name__ == "__main__":
	play_game()
	

    