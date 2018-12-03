class Hangman:
  def __init__(self, word, guessLetter):
    self.word = word
    self.guessedLetter = []
    self.missedLetter = []

  def wordLength(self, word):
    hide = '_'
    wordLength = (hide * len(word))
    return print(wordLength)
  
  def guessLetters(self, letter):
    if letter in ?? and letter not in guessedLetter:
      guessedLetter.append(letter)
    elif letter not in ?? and letter not in missedLetter:
      missedLetter.append(letter)
    else:
      return False
   
  def gameEnd(self):    # Not sure about this function
    while len(missedLetter) < 6:
      return True
    else:
      return False
