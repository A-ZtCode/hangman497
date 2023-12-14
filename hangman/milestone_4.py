# Writing the code for milestone_4.py

import random

# Adding the check_guess and ask_for_input methods to the Hangman class

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
         else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            # More logic will be added here in the next task
        # More conditions will be added here in the next task

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Testing the Hangman class with the new methods
# Assume 'word_list' contains a list of words
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
print("Word to guess:", hangman_game.word)
print("Word guessed so far:", hangman_game.word_guessed)
print("Number of unique letters:", hangman_game.num_letters)
print("Number of lives:", hangman_game.num_lives)
print("List of guesses:", hangman_game.list_of_guesses)
