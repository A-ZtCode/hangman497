import random

# Creating a list of 5 favorite fruits
favorite_fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Assigning the list to a variable called word_list
word_list = favorite_fruits

# Printing out the newly created list
print(word_list)

# Using the random.choice method to select a random word from the word_list
random_word = random.choice(word_list)

# Assigning the randomly generated word to a variable called word
word = random_word

# Printing out the word
print(word)

# Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# Checking if the length of the input is 1 and the input is alphabetical
if len(guess) == 1 and guess.isalpha():
    # Printing a message if the input is valid
    print("Good guess!")
else:
    # Printing a message if the input is not valid
    print("Oops! That is not a valid input.")
