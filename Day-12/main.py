from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The number was: {answer}")
        
def set_difficulty():
    level = input("Choose difficulty, Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to Number Guessing Game.")
    print("I'm thinking numbers between 1 to 100.")
    # Generate random number
    answer = randint(1, 100)
    print(f"Psst! The current number is: {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You've {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out the Guess, You Lose.")
            return
        elif guess != answer:
            print("Guess again")

game()