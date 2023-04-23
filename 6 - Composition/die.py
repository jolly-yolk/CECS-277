import random

class Die:
  """Represents a single die
  Attributes:
    sides (int) - how many sides your die has
    value (int) - the current value of your rolled die"""
  def __init__(self, sides = 6):  
    '''creates the initial values that the class methods will use'''
    self.sides = sides
    self.value = 0
    
  def roll(self): 
    '''rolls the dice and returns whatever random number was rolled'''
    self.value = random.randint(1, self.sides)
    return self.value
    
  def __str__(self): 
    '''returns the value of the dice when the object is used as a string'''
    return str(self.value)
    
  def __lt__(self, other):
    '''returns value if self is less than the value of other (True/False)'''
    if (self.value < other.value):
      return True
    
  def __eq__(self, other):
    '''returns true if both values of self and other are equal'''
    if (self.value == other.value):
      return True
    
  def __sub__(self, other):
    '''returns the difference between value of self and value of other'''
    return self.value - other.value