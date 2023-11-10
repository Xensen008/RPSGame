#Rock, Paper, Scissors — Start your Python learning journey with a simple-but-fun game that everybody knows
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
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
        print("Computer wins!")
    else:
        print("You win!")
        #Main Program
print("Welcome to Rock, Paper, Scissors!")
while True:
    computer_choice = random.randint(0, 2)
    user_choice = get_user_choice()
    determine_winner(computer_choice, user_choice)
    play_again = input("\nDo you want to play again? Enter 'yes' or 'no': ")
    if play_again.lower() != 'yes':
        break
