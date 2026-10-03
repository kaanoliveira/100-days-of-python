# Hangman Project

import random
from hangman_words import word_list
from hangman_art import stages

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

    if guess in correct_letters:
        print(f"You've already guesses {guess}")

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
        print(f"You guesses {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("You lose.")


    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])