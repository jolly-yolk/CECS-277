#Author: Joshua Correa,Nathan Heidari
#Date: 01/31/2023
#Description: Are you smarter than a computer? Why don't you find out with Group 15's Rock, Paper, Scissors! It's the good ol fashion RPS that you know and love but now in Python!

import check_input
import random


def weapon_menu():
  '''This function allows the player to select a weapon or return to the main function. The fucntion uses a while loop and several if statements to return the player's selection.'''
  print('Choose your weapon:')
  print('R. Rock')
  print('P. Paper')
  print('S. Scissors')
  print('B. Back')
  valid = False
  while (valid != True):  #checks for valid input for menu
    select = input()
    if (select == 'R') or (select == 'P') or (select == 'S') or (select
                                                                 == 'B'):
      valid = True
    else:
      continue
  if (select == 'R'):
    return 'Rock'
  elif (select == 'S'):
    return 'Scissors'
  elif (select == 'P'):
    return 'Paper'
  elif (select == 'B'):
    return 'B'


def comp_weapon():
  '''This function's purpose is to allow the computer to select it's own weapon. it uses the random integer module and a few if statements to return the selection.'''
  cweapon = random.randrange(1, 4)  #makes the computer choose a random weapon
  if (cweapon == 1):
    return 'Rock'
  elif (cweapon == 2):
    return 'Paper'
  elif (cweapon == 3):
    return 'Scissors'


def find_winner(player, comp):
  '''This function selects a winner based off the arguements of the player and computer selections. This fucntion is made entirely of if statements that returns a value representing a tie, win, or lose.'''
  if (player == 'Rock') and (comp == 'Scissors'):  #player win when return 1
    return 1
  elif (player == 'Scissors') and (comp == 'Paper'):
    return 1
  elif (player == 'Paper') and (comp == 'Rock'):
    return 1
  elif (comp == 'Rock') and (player
                             == 'Scissors'):  #computer win when return 2
    return 2
  elif (comp == 'Scissors') and (player == 'Paper'):
    return 2
  elif (comp == 'Paper') and (player == 'Rock'):
    return 2
  elif (comp == player):  #tie so return 0
    return 0


def display_scores(player, comp):
  '''This function displays the current score between the computer and the player. The function uses the arguments of the player and computer win values to display the score.'''
  print(f'Player = {player}')
  print(f'Computer = {comp}')


def main():
  '''This is the main function that calls all the other functions as well as formatting the game for the player. The main function calls other functions, uses while statements, if statements, and bool variables.'''
  on = True  #defines RPS active bool, player score, and computer score before loop
  pscore = 0
  cscore = 0
  while (on == True):
    print('RPS Menu')
    print('1. Play Game')
    print('2. Show Score')
    print('3. Quit')
    select = check_input.get_int_range('', 1, 3)
    while (select == 1):
      if (select == 1):  #The game when active
        weapon = weapon_menu()  #player selects weapon
        cweapon = comp_weapon()  #computer selects weapon
        if (weapon == 'B'):  #when the player selects back in the weapon menu
          break
        print(f'You chose {weapon}')
        print(f'Computer chose {cweapon}')
        result = find_winner(weapon, cweapon)  #calculates result
        if (result == 1):
          print('Player wins')
          pscore += 1
        elif (result == 2):
          print('Computer wins')
          cscore += 1
        elif (result == 0):
          print('Tie')
    if (select == 2):  #displays score
      display_scores(pscore, cscore)
    elif (select == 3):  #shows final score and ends program
      print('Final Score')
      display_scores(pscore, cscore)
      on = False


main()