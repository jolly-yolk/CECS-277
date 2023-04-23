import abc

class Monster (abc.ABC):
  '''Represents: an abstract monster class
  Attributes:
    name (str) - name of the monster
    hp (int) - health points
  Monster class abstracts the attributes'''
  def __init__(self, name, hp):
    '''Sets the name and hp using the parameters'''
    self._name = name
    self._hp = hp

  @property
  def hp(self):
    '''returns the monster hp'''
    return self._hp

  @property
  def name(self):
    '''returns the monster name'''
    return self._name

  @abc.abstractmethod
  def attack(self):
    '''Monster attack'''
    pass

  def __str__(self):
    '''Returns the string with the name,hp, and attack power of the monster'''
    return f"Name: {self.name}\nHP: {self.hp}\nAttack: {self.attack()}"

