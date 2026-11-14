
import random

# Predefined list of words
words = ["python", "apple", "coding", "tiger", "robot"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("===== WELCOME TO HANGMAN =====")

while incorrect_guesses < max_guesses:

    display_word = ""

    # Display hidden and guessed letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Remaining chances:", max_guesses - incorrect_guesses)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)

if all(letter in guessed_letters for letter in secret_word):
    print("The word was:", secret_word)
