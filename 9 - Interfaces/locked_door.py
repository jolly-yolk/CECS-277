import door
import random

class LockedDoor (door.Door):
  '''Locked Door randomizes the location of the key'''
  def __init__ (self):
    self._key_location = random.randint(1, 4)
    self._input = 0

  def examine_door (self):
    '''Returns string of description of the door'''
    return 'You encounter a locked door, you must look around for the key.'

  def menu_option (self):
    '''Returns a string of the menu options for door to choose from unlocking the door'''
    return '1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock. \n4. Look in your pocket.'

  def get_menu_max (self):
    '''Returns the number of options in the menu above'''
    return 4

  def attempt (self, option):
    '''Passes user selection value from menu, then updates the attributes that are needed to dertermine door'''
    self._input = option
    if (self._input == 1):
      return 'You look under the mat.'
    elif (self._input == 2):
      return 'You look under the flower pot.'
    elif (self._input == 4):
      return 'Why would it be in your pocket?'
    else:
      return 'You look under the fake rock.'

  def is_unlocked (self):
    '''Checks to see if door was unlocked, which results on returing True or False'''
    if (self._key_location == self._input):
      return True
    else:
      return False

  def clue (self):
    '''Returns a string of a Clue'''
    if (self._input == 4):
      return 'Are you serious? Of course it wasn\'t in your pocket!'
    return 'Maybe try somewhere else?'

  def success (self):
    '''Returns a string of oppening the door sucessfully'''
    if (self._input == 4):
      return 'Oh wow it was actually in your pocket. How did that get there?'
    return 'Congratulations, you looked in the right spot.'