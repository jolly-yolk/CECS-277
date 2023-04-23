import door
import random

class DeadboltDoor (door.Door):
  '''Dead Bolt Door randomizes the state of two bolts that are locked or unlcoked'''
  def __init__(self):
    self._bolt1 = random.randint(0, 1)
    self._bolt2 = random.randint(0, 1)
    self._kick = 0

  def examine_door (self):
    '''returns string of description of the door'''
    return 'You encounter a double deadbolt door, both deadbolts must be unlocked to open it, \nbut you can\'t tell from looking at them whether they\'re locked or unlocked.'

  def menu_option (self):
    '''Returns a string of the menu options for door to choose from unlocking the door'''
    return '1. Toggle Bolt 1\n2. Toggle Bolt 2\n3. Kick the door'

  def get_menu_max (self):
    '''Returns the number of menu options'''
    return 3

  def attempt (self, option):
    '''Passes user selection value from menu, then updates the attributes that are needed to dertermine door'''
    if (option == 1):
      if (self._bolt1 == 0):
        self._bolt1 = 1
      else:
        self._bolt1 = 0
      return 'You toggle the first bolt.'
    elif (option == 3):
      self._kick = 1
      return 'You kick the door.'
    else:
      if (self._bolt2 == 0):
        self._bolt2 = 1
      else:
        self._bolt2 = 0
      return 'You toggle the second bolt.'

  def is_unlocked (self):
    '''Checks to see if door was unlocked, which returns True or False'''
    if (self._bolt1 == self._bolt2 == 1):
      return True
    elif ((self._bolt1 == 1) or (self._bolt2 == 1)) and (self._kick == 1):
      return True
    else:
      return False

  def clue (self):
    '''Returns a string of a clue to opening the door'''
    if (self._bolt1 == 1) or (self._bolt2 == 1):
      return 'You jiggle the door...it seems like one of the bolts is unlocked.'
    elif (self._kick == 1):
      self._kick = 0
      return 'You kick the door but fall down. It\'s very embarrassing.'
    else:
      return '...it seems like it\'s completely locked.'

  def success (self):
    '''Returns a string of sucessfully opening the door'''
    if (self._kick == 1):
      return 'The remaining deadbolt snaps from your kick! It looks really cool!'
    return 'Congratulations, you unlocked all the deadbolts.'