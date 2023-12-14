# Defining the check_guess function
def check_guess(guess):
    # Convert the guess into lower case
    guess = guess.lower()

    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Defining the ask_for_input function
def ask_for_input():
    while True:
        # Asking the user to guess a letter
        guess = input("Please guess a letter: ")

        # Checking if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Call check_guess function
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the ask_for_input function to test the code
ask_for_input()
