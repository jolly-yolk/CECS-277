#Author: Joshua Correa, Nathan Heidari
#Date: 01/24/2023
#Description: Create a Python version of the game "Three Card Monte"
import check_input
import random

def main():      #main
  print('-Three card Monte-')       #Prints Title
  print('Find the queen to double your bet!')    #Prints User to Find Queen
  money = 100                                  #User money set at 100
  while (money > 0):                   #this is the main while loop
    print(f'You have ${money}')        #Introduces the user money balance
    bet = check_input.get_int_range('How much you wanna bet?', 1, money)    #Tells User To Bet
    money -= bet                       #When User Bets Money Is Subtract by that amount
    hidden_cards('1', '2', '3')        #Cards are catorgies into 1,2,3
    guess = check_input.get_int_range('Find the queen:', 1, 3)      #User guesses
    result = reveal_cards(guess)       #From the Guesses result shows answers
    if (result == True):               #If your guess is Correct/True
      print('You got lucky this time...')    #Correct prints you got lucky
      money = money + (2*bet)          #Correct bet gets doubled by 2
    else:
      print('Sorry...you lose.')      #If guess wrong then promopts you lose
      end = check_input.get_yes_no('Play again? (Y/N):')    #Ask if you want to play again
      if (end == False):      #User decison 
        break
      else:
        continue
  if (money <= 0):
    print('You\'re out of money. Beat it loser!')    #Tells User you lost

def hidden_cards(a, b, c):          #Displays Cards
  print('+-----+ +-----+ +-----+')
  print('|     | |     | |     |')
  print(f'|  {a}  | |  {b}  | |  {c}  |')
  print('|     | |     | |     |')
  print('+-----+ +-----+ +-----+')

def reveal_cards(guess):        #Reveals The Hidden Cards
  cards = ['K', 'Q', 'K']
  random.shuffle(cards)         #Shuffle cards
  hidden_cards(cards[0], cards[1], cards[2])
  if (cards[guess - 1] == 'Q'):      #Determines if user picked Q
    return True                  #If Queen was selected returns true
  else:
    return False                  #returns false
      
main()
