import tkinter
import random

window = tkinter.Tk()
window.title("Hangman")
window.geometry("640x400+100+100")

print("This is a simple version of the word game Hangman")
print()
print("The word will be randomly selected from a list and you will have" +
      " X tries to guess all of the letters in the word. Good Luck!")
print()

#This function selects the word. You could add more words or seperate categories here
def selectWord():
  testList = ['test']
  word = random.choice(testList)
  return word

#Function that converts the word selected to a list
def wordList(word):
  wordList = list(word)
  return wordList

#Function that creates a list of blank characters
def blanksList(word):
  blanksList = list('_' * len(word))
  return blanksList

#Function that converts the blank list for the user
def hideWord(blanks_List):
  seperator = ' '
  hiddenStr = seperator.join(blanks_List)
  return hiddenStr

#Validation Function to ensure not guessing multiple letters 
def validGuess(my_guess):
  my_guess = my_guess.lower()
  return (my_guess.isalpha and len(my_guess) == 1)

#Function that performs the process by altering two seperate lists
def guessLetter(my_guess, word, word_List, blanks_List):
  seperator = ' '
  seperator2 = ''


  if my_guess in word_List: 
    count = word_List.count(my_guess) 
      
    for i in range(count):
      guess_index = word_List.index(my_guess)
      guess_letter = word_List.pop(guess_index)
      word_List.insert(guess_index, '*')

      del blanks_List[guess_index]
      blanks_List.insert(guess_index, my_guess) 

    print(seperator.join(blanks_List))

  elif my_guess not in word:
    print("Bad Guess! The letter %s is not in your word." % (my_guess))
     
  return

  def over(self):
    return self.game_done() or (len(self.missed_letters) == 6)
  
  def game_done(self):
    if '_' not in self.hideWord():
      return True
    return False
  

def main():

  #These variables are initialized in the above functions
  word = selectWord()
  word_List = wordList(word)
  blanks_List = blanksList(word)
  hidden_str = hideWord(blanks_List)

  seperator = ''
  #The word they are guessing and input is taken below
  print("Here is your word:", hidden_str)
  print()    
  my_guess = input("Guess a letter that could be in your word"
                   + " or press <Enter> to quit:  ")
  print()
  #This loop needs to essentially complete the game by calling guessLetter until the word is found
  while over():
    while not validGuess(my_guess):
      my_guess = input("Don't Cheat! Enter one letter at a time! Guess again: ")
      print()
      
    guessLetter(my_guess, word, word_List, blanks_List)
    print()
        
    my_guess = input("Guess another letter that could be in your word:  ")
    print()
          
main()
