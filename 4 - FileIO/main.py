#Name: Joshua Correa, Nathan Heidari
#Date: 02/14/23
#Brief Description: Welcome to Maze Solver! Do you have what it takes to solve these diffuclt mazes? Give it your best shot!

import check_input
import random

def read_maze():
  '''This function has no input rather it is a function that reads a maze.txt file. The maze file is selected from the Maze folder and is iterated through adding each row. The output for this function is a 2D list of containing each row of the maze.'''
  level = random.randint(1, 5) #picks a random maze to play
  file = open(f'Mazes/maze{level}.txt') #opens the random maze
  maze = [] #everything below is appending each row of the maze into a list creating a 2D List
  for row in file:
    list = []
    for item in row:
      if item != '' and item != '\n':
        list.append(item)
    print(row)
    maze.append(list)
  file.close()
  return maze
  
def find_start(maze):
  '''This function takes the 2D maze list as an input. The maze is iterated through until it finds the S item which is your starting point. The output is a list with two items: the x and y value for the S.'''
  loc = [] #this function finds S in the maze 2D list and saves its corrdinates
  for row in maze:
      for item in row:
        if (item == 'S'):
          loc.append(maze.index(row) + 1) #x coordinate
          loc.append(row.index(item) + 1) #y coordinate
          return loc

def display_maze(maze, loc):
  '''This function uses the maze 2D list and the list with the x and y value for the Start location. The function iteraties through each row, makes it a string, and then repeats it. The output is the full maze and returns nothing.'''
  maze[loc[0]][loc[1]] = 'X' #makes an X appear where ever the current loc cord is
  for row in maze: #prints out the maze line by line
    line = ''
    for item in row:
      line += item
    print(line)
    
def main():
  '''This function takes no inputs and is a staging ground for all other functions. The function moves the player and checks the conditions for winning. The function also helps with the mystery maze (but its a secret don't tell anyone).'''
  on = True #turns on the game
  print('-Maze Solver-')
  maze = read_maze()
  loc = find_start(maze)
  loc[0] -= 1 #accurately displays x and y cord
  loc[1] -= 1
  origin_x, origin_y = loc[0], loc[1] #saves starting point
  while (on == True):
    if (maze[origin_x][origin_y] != 'S'): #consistantly displays the start point
      maze[origin_x][origin_y] = 'S'
    display_maze(maze, loc)
    print('1. Go North')
    print('2. Go South')
    print('3. Go East')
    print('4. Go West')
    choice = check_input.get_int_range('Enter choice: ', 1, 4) #checks your choice for movement
    
    if (choice == 2):
      if (maze[loc[0] + 1][loc[1]] == '*'): #can't walk through walls position not updated
        print('You cannot move there.')
        continue
        
      elif (maze[loc[0]+1][loc[1]] == 'F') and (len(maze[0]) == 3): #mysterymaze shenanigans
        print('You didn\'t think it would be that easy did you?')
        file = open('Mazes/mysterymaze.txt')
        maze = []
        for row in file:
          list = []
          for item in row:
            if item != '' and item != '\n':
              list.append(item)
          maze.append(list)
        loc = find_start(maze)
        loc[0] -= 1
        loc[1] -= 1
        origin_x, origin_y = loc[0], loc[1]
        
      elif (maze[loc[0] + 1][loc[1]] == 'F'): #when the player reaches the end the game ends
        maze[loc[0]][loc[1]] = ' '
        loc[0] += 1
        maze[loc[0]][loc[1]] = 'X'
        display_maze(maze, loc)
        print('Congratulations! You solved the maze.')
        break #turns off the game
        
      elif (maze[loc[0] + 1][loc[1]] == '?'): #Secrets you can collect! How Exciting!
        maze[loc[0]][loc[1]] = ' '
        loc[0] += 1
        print('Congrats you found the secret! Your so cool!')
        
      else: #moves player and makes sure to delete the previous position X
        maze[loc[0]][loc[1]] = ' '
        loc[0] += 1
        
    elif (choice == 1):
      if (maze[loc[0] - 1][loc[1]] == '*'):
        print('You cannot move there.')
        continue
        
      elif (maze[loc[0] - 1][loc[1]] == 'F'):
        maze[loc[0]][loc[1]] = ' '
        loc[0] -= 1
        maze[loc[0]][loc[1]] = 'X'
        display_maze(maze, loc)
        print('Congratulations! You solved the maze.')
        break
        
      elif (maze[loc[0] - 1][loc[1]] == '?'):
        maze[loc[0]][loc[1]] = ' '
        loc[0] -= 1
        print('Congrats you found the secret! Your so cool!')
        
      else:
        maze[loc[0]][loc[1]] = ' '
        loc[0] -= 1
        
    elif (choice == 3):
      if (maze[loc[0]][loc[1] + 1] == '*'):
        print('You cannot move there.')
        continue
        
      elif (maze[loc[0]][loc[1] + 1] == 'F'):
        maze[loc[0]][loc[1]] = ' '
        loc[1] += 1
        maze[loc[0]][loc[1]] = 'X'
        display_maze(maze, loc)
        print('Congratulations! You solved the maze.')
        break
        
      elif (maze[loc[0]][loc[1] + 1] == '?'):
        maze[loc[0]][loc[1]] = ' '
        loc[1] += 1
        print('Congrats you found the secret! Your so cool!')
        
      else:
        maze[loc[0]][loc[1]] = ' '
        loc[1] += 1
        
    elif (choice == 4):
      if (maze[loc[0]][loc[1] - 1] == '*'):
        print('You cannot move there.')
        continue
        
      elif (maze[loc[0]][loc[1] - 1] == 'F'):
        maze[loc[0]][loc[1]] = ' '
        loc[1] -= 1
        maze[loc[0]][loc[1]] = 'X'
        display_maze(maze, loc)
        print('Congratulations! You solved the maze.')
        break
        
      elif (maze[loc[0]][loc[1] - 1] == '?'):
        maze[loc[0]][loc[1]] = ' '
        loc[1] -= 1
        print('Congrats you found the secret! Your so cool!')
        
      else:
        maze[loc[0]][loc[1]] = ' '
        loc[1] -= 1
main()