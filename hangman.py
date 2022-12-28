stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \

| | | | (_| | | | | (_| | | | | | | (_| | | | |
\
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''


import openai_api
def play_hangman():

    #Intro
    print(logo)
    print("Welcome to hangman!\n")
    print()
    numletters = input("How many letters would you like the word to have?\n")
    print()
    print(f"OK, today's word has {numletters} letters\n")

    # Get a random word
    word = callgpt.askgpt(f"give me a simple english word with {numletters} letters")
    word = word.lower()
    word = word.strip()
    wordlen = len(word)

    counter = 0
    while counter < wordlen:
        print("_ ", end='')
        counter += 1
    print()
    print(stages[6])

    #Make word into list and create list for guesses
    wordlist = list(word)
    guessedword = list("_" * wordlen)

    guesses = 6  # set initial number of guesses to 6
    while guesses > 0:  # continue until guesses run out
        theguess = input("\n\nWhat is your guess?\n\n")
        lowerguess = theguess.lower()
        position = 0
        correct_guess = False  # flag to track if guess is correct
        for letter in wordlist:
            if letter == lowerguess:
                guessedword[position] = letter
                correct_guess = True  # set flag to indicate correct guess
            position = position + 1
        lettersleft = guessedword.count('_')
        if lettersleft == 0:
            print()
            print("Correct!!")
            print("You won!!!")
            print()
            print(f"The word was {word}!!")
            print()
            break  # exit loop
        elif correct_guess == True:
            # correct guess, continue with same number of remaining guesses
            print()
            for item in guessedword:
                print(item, end=' ')
            print()
            print()
            print(f"You have {guesses} guesses left!!")
            print()
            print(stages[guesses])
        else:
            # incorrect guess, decrease number of remaining guesses
            guesses = guesses - 1
            if guesses == 0:
                print()
                print()
                print("You lose!!!")
                print()
                print(stages[0])
                print()
                print(f"The word was {word}")
            else:
                print()
                for item in guessedword:
                    print(item, end=' ')
                print()
                print()
                print(f"You have {guesses} guesses left!!")
                print()
                print(stages[guesses])
# Prompt the player to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == 'y':
        play_hangman()
    else:
        print("Thank you for playing hangman!")


play_hangman()

