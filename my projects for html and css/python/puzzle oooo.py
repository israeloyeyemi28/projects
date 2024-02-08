
# this is a word puzzle and for my creativity i added the name if the programmer below.
# import random means out of any of those words, pick one.


import random

# Define a list of words to be guessed
words = ["jamaica", "israel", "mosiah", "nigeria", "insect"]

# Choose a random word from the list
chosen_word = random.choice(words)

# Convert the chosen word to a list of characters
word_list = list(chosen_word)

# Create a hint by replacing all characters except the first and last with underscores
hint = [word_list[0]] + ["_" for i in range(len(word_list) - 2)] + [word_list[-1]]

# Print welcome message
print("Welcome to the word guessing game!\n")

# Print the initial hint
print("Your hint is: " + " ".join(hint))

# Initialize the number of guesses
num_guesses = 0

# Loop until the word is guessed or the maximum number of guesses is reached
while True:
    # Get a guess from the user
    guess = input("What is your guess? ")

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is the same length as the chosen word
    if len(guess) != len(chosen_word):
        print("Your guess must be the same length as the secret word.")
        continue

    # Check if the guess is correct
    if guess == chosen_word:
        print("Congratulations! You guessed it!")
        print("It took you " + str(num_guesses) + " guesses")
        break

    # If the guess is incorrect, update the hint
    else:
        for i in range(len(word_list)):
            if guess[i] == word_list[i]:
                hint[i] = guess[i].upper()
            elif guess[i] in word_list:
                hint[i] = guess[i].lower()
            else:
                hint[i] = "_"
        print("Your hint is: " + " ".join(hint))
        
        print('This game was created by israel, feel free to play it again.')