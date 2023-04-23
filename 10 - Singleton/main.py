import maze
import minotaur
import hero
import check_input
#Name: Joshua Correa, Nathan Heidari
#Date: 3/14/23
#Description: In this program users are invited to enter an mysterious maze that is guarded by an terrifying ferocious minotaur who guards the maze which is his habitat. The user must bravely travel and maneuver throughout this maze would being spotted by this monster.From this the user must find the exit before the minotaur captures him and would result the user to lose at the game. Are you willing to surive and take on the minotaur by not being spotted and exiting to the finish-line succesfully?

def main():
  '''The main function that creates the objects and facilitates the game. Takes no input. Prompts the user with a difficulty to choose from (Easy to Insane). Asks the user to move in the maze up, down, left, or right, the minotaur(s) then move after the player. This repeats until the minotaur(s) or player wins. Outputs nothing.'''
  maz = maze.Maze()
  her = hero.Hero()
  mino = minotaur.Minotaur()
  insane = False
  print('--Minotaur Maze--')
  mino.diff = check_input.get_int_range('Please Select You Difficulty:\n1. Easy\n2. Medium\n3. Hard\n4. Insane\n', 1, 4)
  if (mino.diff == 4):
    mino2 = minotaur.Minotaur()
    insane = True
    mino.diff = 2
    mino2.diff = 2
  elif (mino.diff == 1):
    mino.diff = 3
  elif (mino.diff == 2):
    mino.diff = 2
  else:
    mino.diff = 1
  
  while True:
    print(maz)
    while True:
      moves = ['W', 'A', 'S', 'D']
      move = input('Choose a Direction (WASD): ')
      move = move.capitalize()
      if (move in moves):
        break
      
    if (move == 'W'):
      action = her.go_up()
      if (action == '*'):
        print('You ran into a wall!')
      elif (action == 'M'):
        print(maz)
        print('You ran into the minotaur!')
        break
      elif (action == 'F'):
        print(maz)
        print('You found the exit!')
        break
        
    elif (move == 'S'):
      action = her.go_down() 
      if (action == '*'):
        print('You ran into a wall!')
      elif (action == 'M'):
        print(maz)
        print('You ran into the minotaur!')
        break
      elif (action == 'F'):
        print(maz)
        print('You found the exit!')
        break
        
    elif (move == 'A'):
      action = her.go_left() 
      if (action == '*'):
        print('You ran into a wall!')
      elif (action == 'M'):
        print(maz)
        print('You ran into the minotaur!')
        break
      elif (action == 'F'):
        print(maz)
        print('You found the exit!')
        break
        
    elif (move == 'D'):
      action = her.go_right() 
      if (action == '*'):
        print('You ran into a wall!')
      elif (action == 'M'):
        print(maz)
        print('You ran into the minotaur!')
        break
      elif (action == 'F'):
        print(maz)
        print('You found the exit!')
        break

    mino_move = mino.move_minotaur()
    if (mino_move == 'H'):
      print(maz)
      print('You ran into the minotaur!')
      break
    
    if (insane == True):
      mino2_move = mino2.move_minotaur()
      if (mino2_move == 'H'):
        print(maz)
        print('You ran into the minotaur!')
        break

main()