import random
#Reminder:
# handle edge cases!
#use linter!
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
    for i in secretWord:
      if not i in lettersGuessed:
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
    print("this is what you have guessed so far", lettersGuessed)
    msg = ""
    for i in secretWord:
      if i in lettersGuessed:
        msg += i
      else:
        msg += " _ "
    return msg







# def getAvailableLetters(lettersGuessed):
#     '''
#     lettersGuessed: list of letters that have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''
#     for i in range(0, len(lettersGuessed)):
#      if lettersGuessed[i] in secretWord:
#       return secretWord.replace("lettersGuessed[i]", "")
#      else:
#       return ""


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
    guessLeft = len(secretWord) + 2
    print("start the game, the number of secretWord letters is", len(secretWord))
    # print("secret word is ", secretWord)
    lettersGuessed = []
    while guessLeft > 0:
      guess = input("guess one letter: ").lower()
      lettersGuessed.append(guess)
      guessLeft -= 1
      if not guess in secretWord:
        print("sorry wrong guess")
        print("all guess try is here", getGuessedWord(secretWord, lettersGuessed))
        print('You can still guess ', guessLeft)
      else:
        print("yay you are rignt")
        print("all guess try is here", getGuessedWord(secretWord, lettersGuessed))
        print('You can still guess ', guessLeft)
        if isWordGuessed(secretWord, lettersGuessed) == True:
          print("Congrats, you won!")
          break
    else:
      return print("sorry your are out of guess, the secret word is ", secretWord)

secretWord = loadWord()
hangman(loadWord())

