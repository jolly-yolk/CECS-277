import player
import check_input
#Name: Joshua Correa, Nathan Heidari
#Date: 02/28/2023
#Description: Yahtzee the age old classic is finally here in Python form! Relive the wonderful board game of old with an all new online interface! Is luck on your side?

def take_turn(player):
  """This is the main function that calls the classes and their methods. The main function is mainly comprised of a loop that keeps the game running until the player decides that they have something better to do(i.e. go outside, watch a movie, laugh with friends, do CECS 277 homework, or play a different board game."""
  print('-Yahtzee-')
  
  print()
  player.roll_dice()
  print(player)
  pair = player.has_pair()
  three = player.has_three_of_a_kind()
  series = player.has_series()
  if (three == True): #these if statements check if the dice fit any of these descriptions
    print('You got 3 of a kind!')
  elif (pair == True):
     print('You got a pair!')
  elif (series == True):
    print('You got a series of 3!')
  else:
    print('Aww.  Too Bad.')
  print(f'Score = {player.get_points()}')
    
  return check_input.get_yes_no('Play again? (Y/N): ')


def main():
  p = player.Player()
  while True:
    x = take_turn(p)
    if (x == True):
      continue
    else:
      break
  print()
  print('Game Over.')
  print(f'Final Score = {p.get_points()}')
main()