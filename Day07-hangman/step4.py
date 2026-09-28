# Hangman Project

import random

stages = [
    """
  +---+
  O   |
 /|\\  |
 / \\  |
     ===
    """,
    """
  +---+
  O   |
 /|\\  |
 /    |
     ===
    """,
    """
  +---+
  O   |
 /|\\  |
      |
     ===
    """,

    """
  +---+
  O   |
 /|   |
      |
     ===
    """,
    """
  +---+
  O   |
  |   |
      |
     ===
    """,
    """
  +---+
  O   |
      |
      |
     ===
    """,
    """
  +---+
      |
      |
      |
     ===
    """
]

# TODO-1 - Create a variable called 'lives' to keep track of the number of lives left. Set lives equal to 6
# TODO-2 - If guess is not a letter in the chosen_word, then reduce lives by 1. If lives goes down to 0 then the game should end, and it should print "You lose"
# TODO-3 - print the ASCII art from the list stages that corresponds to the number of lives the user has remaining


word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter:").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")


    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives]) 