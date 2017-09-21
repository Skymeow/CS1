import random

def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in range(0, len(secretWord)):
      if secretWord[i] in lettersGuessed:
        lettersGuessed.remove(secretWord[i])
      else:
        return False
    return True




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    print_letters = "_"*len(secretWord)
    for i in range(0, len(secretWord)):
      for n in range(0, len(lettersGuessed)):
        if lettersGuessed[n] == secretWord[i]:
          print_letters[i-1:i].replace("_", "lettersGuessed")
          return print_letters
        else:
          return print_letters





def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for i in range(0, len(lettersGuessed)):
     if lettersGuessed[i] in secretWord:
      return secretWord.remove(lettersGuessed[i])
     else:
      return ""


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

     At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    guessLeft = 8
    print("start the game, the number of secretWord letters is", len(secretWord))
    while guessLeft > 0:
      guess = input("guess one letter")
      lettersGuessed = []
      lettersGuessed.append(guess)
      getAvailableLetters(lettersGuessed)
      if lettersGuessed.count(guess) > 1:
        print("oops you have already guessed the word")
      elif guess in secretWord:
        print str("GoodGuess!")+getGuessedWord(secretWord, lettersGuessed)
        if isWordGuessed(secretWord, lettersGuessed) == true:
          return str("Congrats, you won!")
          break
      else:
       guessLeft -= 1
       print str("this is not the right word")+getGuessedWord(secretWord, lettersGuessed)

    else:
      return str("sorry your are out of guess, the secret word is " + str(secretWord))

secretWord = loadWord()
hangman(loadWord())

