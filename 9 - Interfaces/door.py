import abc

class Door (abc.ABC):  
  '''a purely abstract class that acts as the interface'''
  @abc.abstractmethod
  def examine_door(self): #returns string
    '''Returns String for Description of Door'''
    pass
    
  @abc.abstractmethod
  def menu_option(self): #returns string
    '''Return String for Menu options'''
    pass

  @abc.abstractmethod
  def get_menu_max(self): #returns int
    '''Returns the int of menu options'''
    pass

  @abc.abstractmethod
  def attempt(self, option): #returns string
    '''Returns the value selected and updates attributes'''
    pass

  @abc.abstractmethod
  def is_unlocked(self): #returns bool (True/False)
    '''Checks to see if door was unlcoked, True or False'''
    pass

  @abc.abstractmethod
  def clue(self): #returns string
    '''Returns a String for Clues'''
    pass

  @abc.abstractmethod
  def success(self): #returns string
    '''Returns a string of sucessfully opening door'''
    pass