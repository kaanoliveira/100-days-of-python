# Hangman Project

# TODO-1 - Create a "placeholder" with the same number of blanks as the chosen word
# TODO-2 - Create a "display" that puts the guess letter in the right positions and _ in the rest of the string

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"

guess = input("Guess a letter:").lower()
print(guess)

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)