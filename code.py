import random

def get_user_choice():
    """Ask the user for their choice and return it as an integer"""
    while True:
        try:
            choice = int(input("Enter 0 (rock), 1 (paper), or 2 (scissors): "))
            if choice < 0 or choice > 2:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please enter either 0, 1, or 2.")
    return choice

def determine_winner(computer_choice, user_choice):
    """Determine who wins based on the rules of Rock, Paper, Scissors"""
    if computer_choice == user_choice:
        print("It's a tie!")
        return "tie"
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
        print("Computer wins!")
        return "computer"
    else:
        print("You win!")
        return "user"

# Main Program
print("Welcome to Rock, Paper, Scissors!")
computer_score = 0
user_score = 0

while True:
    computer_choice = random.randint(0, 2)
    user_choice = get_user_choice()
    winner = determine_winner(computer_choice, user_choice)
    
    if winner == "computer":
        computer_score += 1
    elif winner == "user":
        user_score += 1
    
    print("Computer score:", computer_score)
    print("Your score:", user_score)
    
    play_again = input("\nDo you want to play again? Enter 'yes' or 'no': ")
    if play_again.lower() != 'yes':
        break