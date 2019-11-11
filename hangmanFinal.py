import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
        
def isLetterGuessed(guess, secretWord):
    '''
    guess: char, user's current guess
    secretWord: string, the word the user is guessing
    returns: boolean, True if the guess is in the lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
       if guess == char:
           return True
    return False
          
def isLetterAlreadyGuessed(guess, lettersGuessed):
    '''
    guess: char, the letter the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if the current guess is in lettersGuessed;
      False otherwise
    '''
    for letter in lettersGuessed:
        if guess == letter:
            return True
    return False

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    matches = 0
    guesses = {}
    for letter in lettersGuessed:
        if letter in guesses:
            guesses[letter] +=1
        else:
            guesses[letter] =1
        for char in secretWord:
              if letter == char and guesses[letter] == 1:
                 matches += 1
             
    if len(secretWord) == matches:
        return True
    else:
        return False

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    #Donna M. Gavin 2/7/2017
    s = []
    abcs = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0,
            'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0,
            's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for letter in lettersGuessed:
        if letter in abcs:
            abcs[letter] +=1
        else:
            abcs[letter] =1
    for k in abcs:
        if abcs[k] == 0:
            s.append(k)
    s.sort()
    answer = ''.join(s)
    return answer

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    #Donna M Gavin, 2/7/2017
    s = []
    for index in range(len(secretWord)):
        s.append('_')
    #print(s)
    guesses = {}
    for letter in lettersGuessed:
        if letter in guesses:
            guesses[letter] +=1
        else:
            guesses[letter] =1
        index = 0
        for index in range(len(secretWord)):
              if secretWord[index] == letter and guesses[letter] == 1:
                 s[index] = letter
              #print(s)
    answer = ''.join(s)
    return answer

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    #Donna M Gavin, 2/8/2017
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ", len(secretWord)," letters long.")
    print("-------------")
    numGuesses = 8
    print("You have ", numGuesses, " guesses left.")
    availableLetters = getAvailableLetters(lettersGuessed)
    print("Available letters: ", availableLetters )
    guess = input("Please guess a letter: ")
    while (not (isWordGuessed(secretWord, lettersGuessed)) and (numGuesses > 0)):
       if (isLetterAlreadyGuessed(guess, lettersGuessed)):
           print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
           print("------------")
       else:
           lettersGuessed.append(guess)
           if (isLetterGuessed(guess, secretWord)):
               print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
               print("------------")
           else:
               numGuesses -= 1
               print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
               print("------------")
       if (not (isWordGuessed(secretWord, lettersGuessed)) and (numGuesses > 0)):
          print("You have ", numGuesses, " guesses left.")
          availableLetters = getAvailableLetters(lettersGuessed)
          print("Available letters: ", availableLetters)
          guess = input("Please guess a letter: ") 
           
       
    if (numGuesses == 0):
        print("Sorry, you ran out of guesses. The word was ", secretWord)
    else:
        print("Congratulations, you won!")


def main():
    # Load the list of words into the variable wordlist
    # so that it can be accessed from anywhere in the program
    wordlist = loadWords()
    secret = chooseWord(wordlist)
    hangman(secret)

    
if __name__ == "__main__":
    main()
