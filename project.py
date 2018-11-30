class Hangman:
  def __init__(self, word, guessLetter):
    self.word = word
    self.guessedLetter = []

  def wordLength(self, word):
    hide = '_'
    wordLength = (hide * len(word))
    return print(wordLength)
    
    
