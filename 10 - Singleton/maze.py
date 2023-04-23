import random
class Maze:
  '''Represents a maze.
  Attributes:
  _maze (2D list) - the contents of the maze in the form of a 2D list
  _instance (object) - holds the single instance of the class because this class is a singleton
  _inititalized (bool) - holds the bool telling whether or not the class has been created already'''
  _instance = None
  _initialized = False
  
  def __new__ (cls):
    '''Takes the class as an input. Checks whether the class has an instance, if not an instance is created. Outputs the instance of the class.'''
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__ (self):
    '''Takes no input. Creates the initial instance of the class. If an instance has been created then nothing happens. If an instance has not been created, the file holding the maze is read and stored in the _maze variable. The _initialized bool is set to True showing that the single instance has been created.'''
    if (not Maze._initialized):
      i = random.randint(1, 2)
      file = open(f'maze-{i}.txt')
      self._maze = [] #everything below is appending each row of the maze into a list creating a 2D List
      for row in file:
        line = []
        for item in row:
          if (item != ''):
            line.append(item)
        self._maze.append(line)
      file.close()
      Maze._initialized = True

  def __getitem__ (self, row):
    '''Takes the index for a wanted row as an input. Outputs the contents in that row as a list'''
    return self._maze[row]

  def __len__ (self):
    '''Takes no input. Outputs the number of rows in the maze.'''
    return len(self._maze)

  def __str__ (self):
    '''Takes no input. Outputs the contents of the maze as a string.'''
    string = ''
    for row in self._maze:
      for item in row:
        string += item
    return string
      

  def find_start (self):
    '''Takes no input. Outputs the starting location designated by an "S" in the initial txt file.'''
    start = []
    for row in self._maze:
      if ('S' not in row):
        continue
      start.append(self._maze.index(row))
      for item in row:
        if (item == 'S'):
          start.append(row.index(item))
    return start
        