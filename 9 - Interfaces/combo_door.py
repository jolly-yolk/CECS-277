import door
import random
class ComboDoor (door.Door):
  '''Combo Door class randomizes a value to a number of 1-10 which upon selecting the correct number opens the door'''
  def __init__(self):
    self._max = 100
    self._min = 1
    self._input = 0
    self._correct_value = random.randint(self._min, self._max)

  def examine_door (self):
    '''Returns the sting Descriptions of the Door'''
    return f'You encounter a door locked with a combination, the combination is a number {self._min} - {self._max}.'

  def menu_option (self):
    '''Returns a string of the menu options for door to choose from when unlocking door'''
    return f'Enter # {self.get_menu_min()} - {self.get_menu_max()}:'

  def get_menu_max (self):
    '''Returns the number of options in the menu'''  
    if (self._correct_value < self._input): #if the player decision is more than the correct decision it becomes the new maximum
      self._max = self._input - 1 #minus 1 because the player decision isn't correct so the next lowest must be the new inclusive maximum
      return self._max
      
    else: #if the player chooses a number less than the correct decision the maximum remains the same
      return self._max
          
  def get_menu_min (self):
    '''This method is special to this class and is not apart of the door interface. It returns the minimum value the player can choose based on what they've already chosen.'''
    if (self._correct_value > self._input): #if the player decision is less than the correct decision it becomes the new minimum
      self._min = self._input + 1 #plus 1 because the player decision isn't correct so the next highest must be the new inclusive minimum
      return self._min
    else: #if the player chooses a number higher than the correct decision the minimum remains the same
      return self._min

  def attempt (self, option):
    '''Passes user selection value from menu, then updates the attributes that are needed to dertermine opening the door'''
    self._input = option
    return f'You turn the dial to ... {self._input}'

  def is_unlocked (self):
    '''Checks to see if door was unlocked, which returns True or False'''
    if (self._input == self._correct_value):
      return True
    else:
      return False

  def clue (self):
    '''Returns the String of Clue'''
    if (self._input < self._correct_value):
      return 'Maybe try a higher value.'
    else:
      return 'Maybe try a lower value.'

  def success (self):
    '''Returns string of door opening'''
    return 'Congratulations, you found the combination.'