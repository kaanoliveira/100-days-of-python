# Hangman Project

# TODO-1 - Use a while loop to let the user guess again
# TODO-2 - Change the for loop so that you keep the previous correct guess and the new letter and add all of that to our variable "display"

import random
word_list = ["aardvark", "baboon", "camel"]

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

    if "_" not in display:
        game_over = True
        print("You win!")