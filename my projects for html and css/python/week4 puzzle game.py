# this is a word puzzle and for my creativity i added the name if the programmer below.
# import random means out of any of those words, pick one and I added some emoji:
    
print("         Welcome to word guessing game👋👋 \nwarning this game is only for those with high IQ😁😁")

print()

print(" In this game, the user would be questioned for series of words . The program would notify you if you got the word right or wrong, it would also ask you if you want to continue the game or not \nGOODLUCK👋👋")

import random

#variable for if I want to keep playing
keep_playing = 'yes'

while keep_playing.lower() == 'yes':
    # Define a list of words to be guessed
    words = ["nigeria", "burnaboy", "microsoft", "conjugate"," byupathway","respect", "rose", "favour", "Israel" ]

    # Choose a random word from the list of words above 
    chosen_word = random.choice(words)

    # Convert the chosen word to a list of letters
    word_list = list(chosen_word)

    # Create a hint by replacing all characters with underscores
    hint = ["_" for i in range(len(word_list)-0)]


    print()

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
            print(f"It took you {num_guesses} guesses")
            break

        # If the guess is incorrect, update the hint till the user gets it right
        else:
            for i in range(len(word_list)):
                if guess[i] == word_list[i]:
                    hint[i] = guess[i].upper()
                elif guess[i] in word_list:
                    hint[i] = guess[i].lower()
                else:
                    hint[i] = "_"
            print("Your hint is: " + " ".join(hint))
    
    # ask if they want to play again
    keep_playing = input('Did you want to keep playing?\n Yes/No? ')

print()


print("THIS GAME HAS SHOWN HOW HIGH YOUR INTELLIGENCE QUOTIENT IS\nKEEP IT UP 👍🏿👍🏿👍🏿")
print(" THANKS FOR PLAYING MY GAME")