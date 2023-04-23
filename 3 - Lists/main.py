#Name: Joshua Correa, Nathan Heidari
#Date: 02/07/2023
#Brief Description: Hangman in Python? They said it couldn't be done...nevertheless here it is! Can you save the little man before he meets a grim fate find out now!

import random
import check_input
from dictionary import words

def display_gallows(num_incorrect):
  '''Outputs the gallow corresponding to the number of incorrect guess the player has. The gallow starts empty and ends (possibly) with a hanged man.'''
  if (num_incorrect == 0): #each if statement displays a different hangman based on the incorrect number of guesses.
    print('========')
    print('||/   | ')
    print('||')
    print('||')
    print('||')
    print('||')
    
  elif (num_incorrect == 1):
    print('========')
    print('||/   | ')
    print('||    o ')
    print('||')
    print('||')
    print('||')
    
  elif (num_incorrect == 2):
    print('========')
    print('||/   | ')
    print('||    o ')
    print('||    | ')
    print('||')
    print('||')
    
  elif (num_incorrect == 3):
    print('========')
    print('||/   | ')
    print('||    o ')
    print('||    | ')
    print('||   /  ')
    print('||      ')
    
  elif (num_incorrect == 4):
    print('========')
    print('||/   | ')
    print('||    o ')
    print('||    | ')
    print('||   / \ ')
    print('||      ')
    
  elif (num_incorrect == 5):
    print('========')
    print('||/   | ')
    print('||   \o ')
    print('||    | ')
    print('||   / \ ')
    print('||      ')
    
  elif (num_incorrect == 6):
    print('========')
    print('||/   | ')
    print('||   \o/')
    print('||    | ')
    print('||   / \ ')
    print('||      ')
  
def display_correct(correct):
  '''Outputs the correct guess, they are either underscores for yet to be guessed letters or letters for correct guesses. The input is a list of the letters and underscores in the correct positions.'''
  for i in range(len(correct)): #displays the correct letters in a sequential row.
    if (i == len(correct)):
      print(correct[i])
    else:
      print(correct[i], end = ' ')
  print()
  
def display_incorrect(incorrect):
  '''The output is a display of incorrect letters that have been guessed by the player and collected in a list. The input is a list of letters that have been collected in the main() function.'''
  incorrect.sort() #puts the incorrect guesses in alphabetical order
  print('Incorrect selections', end = ': ')
  for i in range(len(incorrect)): #displyas the incorrect guess in a sequential order
    if (i == len(incorrect)):
      print(incorrect[i])
    else:
      print(incorrect[i], end = ' ')
  print()
  
def display_letters_remaining(incorrect, correct):
  '''The output is a display of letters that have yet to be guessed by the player, starts as whole alphabet. The inputs are two lists of correct and incorrect guesses that way we can take them out of the remaining letters display.'''
  alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  for i in range(len(incorrect)): #removes incorrect guesses from alphabet
    if (incorrect[i] in alphabet):
      alphabet.remove(incorrect[i])

  for i in range(len(correct)):#removes correct guesses from alphabet
    if (correct[i] in alphabet):
      alphabet.remove(correct[i])

  print('Letters remaining', end = ': ')
  for i in range(len(alphabet)): #displays the remianing letters
    if (i == len(alphabet)):
      print(alphabet[i])
    else:
      print(alphabet[i], end = ' ')
  print()
  
  
def main():
  '''The main function has no inputs and is instead the functiom where all other functions are called that way they can remain organized and modular.'''
  i = True
  while (i == True):
    print('-Hangman-')
    print()
    num_incorrect = 0
    cword = list(random.choice(words)) #chooses a random word from dictionary
    incorrect = []
    correct = ['_', '_', '_', '_', '_']
    on = True

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    while (on == True):
      display_incorrect(incorrect)
      print()
      display_gallows(num_incorrect)
      print()
      display_correct(correct)
      print()
      display_letters_remaining(incorrect, correct)
      print()
    
      selection = input('Enter a letter: ')
      selection = selection.upper() #makes selection uppercase
      if (alphabet.__contains__(selection) == False): #makes sure the selection is in the alphabet
        print('That is not a letter.')
        continue
      
      elif (selection in correct) or (selection in incorrect): #makes sure the selection hasn't already been guessed
        print('You have already used that letter.')
        continue
      
      if (selection in cword):
        print('Correct!')
        print()
        for i in range(len(cword)): #replaces the empty space in correct with the selection
          if (cword[i] == selection):
            correct[i] = selection
      
      elif (selection not in cword): #appends the selection to incorrect guess list and increments the number of incorrect guesses.
        print('Incorrect!')
        print()
        incorrect.append(selection)
        num_incorrect += 1
    
      if (cword == correct): #you win and are shown the results and asked to play again.
        display_gallows(num_incorrect)
        display_correct(correct)
        print()
        print('You win!')
      
        i = check_input.get_yes_no('Play again (Y/N)? ')
      
        if (i == False):
          break
        elif (i == True):
          print()
          break
      
      elif (num_incorrect == 6):#you lose and are shown the results and asked to play again.
        display_gallows(num_incorrect)
        
        for i in range(len(correct)):
          correct[i] = cword[i]
          
        display_correct(correct)
        print()
        print('You lose!')
      
        i = check_input.get_yes_no('Play again (Y/N)? ')
      
        if (i == False):
          break
          
        elif (i == True):
          print()
          break    
main()