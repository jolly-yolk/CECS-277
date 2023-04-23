import door
import random

class CodeDoor(door.Door):
  '''Code door randomize each  characters in the code as X or O'''
  def __init__(self):
    self._correct_code = []
    chars = ['X', 'O']
    for i in range(3):
      self._correct_code.append(random.choice(chars))
    self._input = ['O', 'O', 'O']

  def examine_door (self):
    '''Returns string of description of the door'''
    return 'You encounter a code door, there is a coded keypad with three characters. \nEach key toggles a value with an \'X\' or an \'O\'.'

  def menu_option (self):
    '''Returns a string of the menu options for door to choose from when unlocking door'''
    return '1. Press Key 1\n2. Press Key 2\n3. Press Key 3'

  def get_menu_max (self):
    '''Returns the number of options in the menu'''
    return 3

  def attempt (self, option):
    '''Passes user selection value from menu, then updates the attributes that are needed to dertermin door'''
    if (option == 1):
      if (self._input[0] == 'O'):
        self._input[0] = 'X'
      else:
        self._input[0] = 'O'
      return 'You press key 1'
    
    elif (option == 2):
      if (self._input[1] == 'O'):
        self._input[1] = 'X'
      else:
        self._input[1] = 'O'
      return 'You press key 2'

    elif (option == 3):
      if (self._input[2] == 'O'):
        self._input[2] = 'X'
      else:
        self._input[2] = 'O'
    return 'You press key 3'
      
  def is_unlocked (self):
    '''Checks to see if door was unlocked, which returns True or False'''
    if (self._correct_code == self._input):
      return True
    else:
      return False

  def clue (self):
    '''Returns a string of Clue that would lead to opening the door'''
    clue = ''

    if (self._correct_code[0] == self._input[0]):
      clue += 'The first character seems to be correct.'
    else:
      clue += 'I don\'t think the first character is correct.'
      
    if (self._correct_code[1] == self._input[1]):
      if (len(clue) != 0):
        clue += '\n'
      clue += 'The second character seems to be correct.'
    else:
      if (len(clue) != 0):
        clue += '\n'
      clue += 'I don\'t think the second character is correct.'

    if (self._correct_code[2] == self._input[2]):
      if (len(clue) != 0):
        clue += '\n'
      clue += 'The third character seems to be correct.'
    else:
      if (len(clue) != 0):
        clue += '\n'
      clue += 'I don\'t think the third character is correct.'
      
    return clue
    
  def success (self):
    '''Returns string of successfully openning the door'''
    return 'Congratulations, you found the code.'