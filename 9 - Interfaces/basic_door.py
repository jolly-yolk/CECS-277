import door
import random

class BasicDoor(door.Door):
  '''Establishes the Basic Door class'''
  def __init__ (self):
    self._state = random.randint(1, 2)
    self._input = 0

  def examine_door(self):
    '''Returns string of description of the door'''
    return 'You encounter a basic door, you can either push it or pull it to open.'

  def menu_option(self):
    '''Returns a string of the menu options for door to choose from unlocking the door'''
    return '1. Push\n2. Pull\n3. Knock'

  def get_menu_max(self):
    '''Returns the number of options in the menu'''
    return 3

  def attempt(self, option):
    '''Passes user selection value from menu, then updates the attributes that are needed to determine door'''
    self._input = option
    if (self._input == 1):
      return 'You push the door.'
    elif (self._input == 3):
      return 'You knock on the door.'
    else:
      return 'You pull the door.'
    
  def is_unlocked(self):
    '''Checks to see if door was unlocked, which returns True or False'''
    if (self._input == self._state):
      return True
    else:
      return False

  def clue(self):
    '''Returns a string of Clue'''
    if (self._input == 3):
      return 'No one answers. You feel lonely.'
    return 'Maybe try the other way?'

  def success(self):
    '''Returns string of door opening'''
    return 'Congratulations, you opened the door.'