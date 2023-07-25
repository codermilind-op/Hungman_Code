import random

# define a list of words
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# select a random word from the list
word = random.choice(words)

# create a list to store the correct guesses
correct_guesses = []

# create a list to store the incorrect guesses
incorrect_guesses = []

# create a variable to store the number of incorrect guesses allowed
MAX_INCORRECT_GUESSES = 6

# loop until the player wins or loses
while len(incorrect_guesses) < MAX_INCORRECT_GUESSES:
    # display the current status of the word
    for letter in word:
        if letter in correct_guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

    # ask the player to guess a letter
    guess = input('Guess a letter: ')

    # check if the letter has already been guessed
    if guess in correct_guesses or guess in incorrect_guesses:
        print('You already guessed that letter. Try again.')
    # check if the letter is in the word
    elif guess in word:
        correct_guesses.append(guess)
        print('Good guess!')
        # check if the player has won
        if set(correct_guesses) == set(word):
            print('Congratulations! You won!')
            break
    # if the letter is not in the word
    else:
        incorrect_guesses.append(guess)
        print('Oops! That letter is not in the word.')
        print('Incorrect guesses:', incorrect_guesses)
    print()

# if the player has made too many incorrect guesses
if len(incorrect_guesses) == MAX_INCORRECT_GUESSES:
    print('Sorry, you lost. The word was', word)
