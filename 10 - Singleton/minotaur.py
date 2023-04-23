import random
import maze

class Minotaur:
  '''Represents the monster that is guarding the maze.
  Attributes:
    _row (int) - the x coordinate for the minotaur chosen randomly.
    _col (int) - the y coordinate for the minotaur chosen randomly
    _dir (char) - the direction that the minotaur is going (i.e. U, D, L, R)
    _prev_dir (list) - holds the previous coordinate for the minotaur
    _turns (int) - holds how many turns the minotaur has taken since changing directions
    _diff (int) - the difficulty of the minotaur'''
  def __init__(self):
    '''Takes no input. Randomizes the starting location position of the minotaur to any avaiable blank space in the maze and places an M. Initializes all the other variables to their designated type. Outputs nothing'''
    while True:
      self._row = random.randint(0, len(maze.Maze()) - 2) #int
      self._col = random.randint(0, len(maze.Maze()[0]) - 2) #int
      if (maze.Maze()[self._row][self._col] != '*') and (maze.Maze()[self._row][self._col] != 'H') and (maze.Maze()[self._row][self._col] != 'F') and (maze.Maze()[self._row][self._col] != 'M'):
        maze.Maze()._maze[self._row][self._col] = 'M'
        break   
    self._dir = '' #char
    self._prev_dir = [self._row, self._col] #list
    self._turns = 0 #int
    self._diff = 0 #int

  @property
  def diff (self):
    '''Getter for the diff variable.'''
    return self._diff

  @diff.setter
  def diff (self, diff):
    '''Setter for the diff variable.'''
    self._diff = diff
    
  def _get_search_dir(self):
    '''Takes no input. Chooses the direction of the minotaur will move in by finding the hero's direction. Sets the direction for the minotaur and outputs nothing.'''
    hero_dir = [] #finds the coordinates for the hero
    for row in maze.Maze():
      if ('H' not in row):
        continue
      hero_dir.append(maze.Maze()._maze.index(row))
      for item in row:
        if (item == 'H'):
          hero_dir.append(row.index(item))
          break
          
    if (hero_dir[0] < self._row) and (maze.Maze()[self._row - 1][self._col] != '*'): #relative to the hero's position the minotaur will move
      self._dir = 'U'
    elif (hero_dir[0] > self._row) and (maze.Maze()[self._row + 1][self._col] != '*'):
      self._dir = 'D'
    elif (hero_dir[1] > self._col) and (maze.Maze()[self._row][self._col + 1] != '*'):
      self._dir = 'R'
    elif (hero_dir[1] < self._col) and (maze.Maze()[self._row][self._col - 1] != '*'):
      self._dir = 'L'
    else: #if the minotaur is stuck in a corner then it will try to find its way out
      possible = 0
      for i in range(4):
        if (possible == 0):
          if (maze.Maze()[self._row - 1][self._col] != '*') and (self._prev_dir != [self._row - 1, self._col]):
            self._prev_dir = [self._row - 1, self._col]
            self._dir = 'U'
            break
          else:
            possible += 1
        elif (possible == 1):
          if (maze.Maze()[self._row + 1][self._col] != '*') and (self._prev_dir != [self._row + 1, self._col]):
            self._prev_dir = [self._row + 1, self._col]
            self._dir = 'D'
            break
          else:
            possible += 1
        elif (possible == 2):
          if (maze.Maze()[self._row][self._col + 1] != '*') and (self._prev_dir != [self._row, self._col + 1]):
            self._prev_dir = [self._row, self._col + 1]
            self._dir = 'R'
            break
          else:
            possible += 1
        elif (possible == 3):
          if (maze.Maze()[self._row][self._col - 1] != '*') and (self._prev_dir != [self._row, self._col - 1]):
            self._prev_dir = [self._row, self._col - 1]
            self._dir = 'L'
            break
          else:
            possible += 1
        
        

  def move_minotaur (self):
    '''Takes no input. For every certain number of turns (relative to the difficulty) the minotaur will use the direction gained from the _get_search_dir function to update position. Outputs the item that was previously where the minotaur currently is.'''
    if (self._diff != 1): #the number of turns to change direction is realtive to the difficulty selected in main
      if (self._turns % self._diff == 0):
        self._get_search_dir()
        self._turns = 0
    else:
      if (self._turns % 2 == 0):
        self._get_search_dir()
        self._turns = 0
    self._turns += 1

    if (self._dir == 'U') and (maze.Maze()[self._row - 1][self._col] != '*') and (maze.Maze()[self._row - 1][self._col] != 'F') and (maze.Maze()[self._row - 1][self._col] != 'M'): #Up
      prev = maze.Maze()[self._row - 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row -= 1
      maze.Maze()[self._row][self._col] = 'M'
      return prev
      
    elif (self._dir == 'D') and (maze.Maze()[self._row + 1][self._col] != '*') and (maze.Maze()[self._row + 1][self._col] != 'F')and (maze.Maze()[self._row + 1][self._col] != 'M'): #Down
      prev = maze.Maze()[self._row + 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row += 1
      maze.Maze()._maze[self._row][self._col] = 'M'
      return prev
      
    elif (self._dir == 'L') and (maze.Maze()[self._row][self._col - 1] != '*') and (maze.Maze()[self._row][self._col - 1] != 'F') and (maze.Maze()[self._row][self._col - 1] != 'M'): #Left
      prev = maze.Maze()._maze[self._row][self._col - 1]
      maze.Maze()._maze[self._row][self._col] = ' '
      self._col -= 1
      maze.Maze()[self._row][self._col] = 'M'
      return prev
      
    elif (self._dir == 'R') and (maze.Maze()[self._row][self._col + 1] != '*') and (maze.Maze()[self._row][self._col + 1] != 'F')and (maze.Maze()[self._row][self._col + 1] != 'M'): #Right
      prev = maze.Maze()[self._row][self._col + 1]
      maze.Maze()[self._row][self._col] = ' '
      self._col += 1
      maze.Maze()[self._row][self._col] = 'M'
      return prev

    else:
      return maze.Maze()[self._row][self._col] #if no where to move just return current location item