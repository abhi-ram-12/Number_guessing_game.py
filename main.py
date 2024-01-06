from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Creating a function to guess users against actual answer.


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You've got it the answer was {answer}.")

# Creating a function to choose the difficulty.


def choose_difficulty():
    level = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Choosing a random number between 1 & 100


def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 & 100")
    answer = randint(1, 100)
    print(f"Pssst, The correct answer is {answer}")

    turns = choose_difficulty()

    # Repeating the gussing function if the user looses the game.

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
    # asking user to guess a number.
        guess = int(input("Make a guess: "))

    # track the number of attempts left.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
