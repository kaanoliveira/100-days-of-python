# Number Guessing Game

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(guess, answer):
    if guess > answer:
        return "high"
    elif guess < answer:
        return "low"
    else:
        return "correct"

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    answer = randint(1, 100)

    if difficulty == "easy":
        attempts = EASY_LEVEL_TURNS
    else:
        attempts = HARD_LEVEL_TURNS
    print(f"You have {attempts} attempts remaining to guess the answer.")

    while attempts > 0:
        guess = int(input("Make a guess: "))
        result = check_guess(guess, answer)

        if result == "correct":
            print(f"You got it! The answer was {answer}.")
            return
        elif result == "high":
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses.")
            return
        else:
            if attempts == 1:
                print(f"You have {attempts} attempt remaining.")
            else:
                print(f"You have {attempts} attempts remaining.")


play_game()

