'''
READ THIS:

Jeanna,

This is a basic version of Hangman that I did today. It has no GUI components
and still needs a few things to be added before we move to the GUI issues.

I should note that I will not have time to work on this tomorrow (Saturday).  \
If you do have time, here are some things you could work on:

1. Repeated Letters - I cannot figure out a way for the program with guessing
the same letter twice i.e. guessing t multiple times. I think this can be
fixed with a validation function of some sorts.

2. Ending the game - Once the word has been entirely guessed, we need to
figure out a way to end the game.Try adding to the "guessLetter" function
or to the while loop in the "main()".

3. Anything else you see fit to add - add more words and categories, a function
to draw the hangmans, etc.

**It should be noted that right now,the only word the program functions with
is 'test'.

If you have any questions, text or email me and look at the design comments

Best regards, 

Neil 
'''
import random

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
  while my_guess:
    while not validGuess(my_guess):
      my_guess = input("Don't Cheat! Enter one letter at a time! Guess again: ")
      print()
      
    guessLetter(my_guess, word, word_List, blanks_List)
    print()
        
    my_guess = input("Guess another letter that could be in your word:  ")
    print()
          
main()






  


    



    
