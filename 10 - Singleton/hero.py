import maze

class Hero:
  '''Represents the hero which is the User Playable Character.
  Attributes:
    _row (int) - x coordinate for the hero
    _col (int) - y coordinate for the hero'''
  def __init__(self):
    '''This sets the hero starting locating by establishing the row and col attributes to the maze which then places an H on that spot'''
    self._row = maze.Maze().find_start()[0] #int
    self._col = maze.Maze().find_start()[1] #int
    maze.Maze()._maze[self._row][self._col] = 'H'

  def go_up(self):
    '''Takes no input. Updating the heros locating by subtracting 1 to go up on the row only if there is not a wall, which then overwrites the old H and places a new H for the updated position. Outputs the item that was previously where the hero currently is.'''
    if (maze.Maze()[self._row - 1][self._col] == ' '):
      prev = maze.Maze()[self._row - 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row -= 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
      
    elif (maze.Maze()[self._row - 1][self._col] == 'M'): #if you run into minotaur then you lose
      prev = maze.Maze()[self._row - 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row -= 1
      maze.Maze()[self._row][self._col] = 'M'
      return prev
      
    elif (maze.Maze()[self._row - 1][self._col] == 'F'): #if you run into exit then you win
      prev = maze.Maze()[self._row - 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row -= 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
      
    else:
      return '*'

  def go_down(self): #returns char
    '''Takes no input. Updating the heros locating by adding 1 to go down on the row only if there is not a wall, which then overwrites the old H and places a new H for the updated position. Outputs the item that was previously where the hero currently is.'''
    if (maze.Maze()[self._row + 1][self._col] == ' '):
      prev = maze.Maze()[self._row + 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row += 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
      
    elif (maze.Maze()[self._row + 1][self._col] == 'M'):
      prev = maze.Maze()[self._row + 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row += 1
      maze.Maze()[self._row][self._col] = 'M'
      return prev
      
    elif (maze.Maze()[self._row + 1][self._col] == 'F'):
      prev = maze.Maze()[self._row + 1][self._col]
      maze.Maze()[self._row][self._col] = ' '
      self._row += 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
    else:
      return '*'
      
  def go_left(self): #returns char
    '''Takes no input. Updating the heros locating by subtracting 1 to go left on the col only if there is not a wall, which then overwrites the old H and places a new H for the updated position. Outputs the item that was previously where the hero currently is.'''
    if (maze.Maze()[self._row][self._col - 1] == ' '):
      prev = maze.Maze()[self._row][self._col - 1]
      maze.Maze()[self._row][self._col] = ' '
      self._col -= 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
      
    elif (maze.Maze()[self._row][self._col - 1] == 'M'):
      prev = maze.Maze()[self._row][self._col - 1]
      maze.Maze()[self._row][self._col] = ' '
      self._col -= 1
      maze.Maze()[self._row][self._col] = 'M'
      return prev
      
    elif (maze.Maze()[self._row][self._col - 1] == 'F'):
      prev = maze.Maze()[self._row][self._col - 1]
      maze.Maze()[self._row][self._col] = ' '
      self._col -= 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
    else:
      return '*'

  def go_right(self): #returns char
    '''Takes no input. Updating the heros locating by adding 1 to go left on the col only if there is not a wall, which then overwrites the old H and places a new H for the updated position. Outputs the item that was previously where the hero currently is.'''
    if (maze.Maze()[self._row][self._col + 1] == ' '):
      prev = maze.Maze()[self._row][self._col + 1]
      maze.Maze()[self._row][self._col] = ' '
      self._col += 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
      
    elif (maze.Maze()[self._row][self._col + 1] == 'M'):
      prev = maze.Maze()[self._row][self._col + 1]
      maze.Maze()[self._row][self._col] = ' '
      self._col += 1
      maze.Maze()[self._row][self._col] = 'M'
      return prev
      
    elif (maze.Maze()[self._row][self._col + 1] == 'F'):
      prev = maze.Maze()[self._row][self._col + 1]
      maze.Maze()[self._row][self._col] = ' '
      self._col += 1
      maze.Maze()[self._row][self._col] = 'H'
      return prev
    else:
      return '*'