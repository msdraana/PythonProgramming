from logo import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system("clear")


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def Check_answer(guess, a_follower_count, b_follower_count):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    # account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    # if account_a == account_b:
    #     account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    print(a_follower_count)
    b_follower_count = account_b["follower_count"]
    print(b_follower_count)
    is_correct = Check_answer(guess, a_follower_count, b_follower_count)
    
    clear()
    print(logo)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong, Final score: {score}")

    # Score keeping 


# Making account at position B become the next account at position A

# clear the screen
