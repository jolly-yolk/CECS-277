import abc

class Entity (abc.ABC):
  '''Represents an abstract entity
  Attributes:
    name (str) - whater the entity is called
    hp (int) - whatever the entities hit points are
    og_hp (int) - save the initial hp value so that you can use it in the string'''
  def __init__(self, name, hp):
    self._name = name
    self._hp = hp
    self._og_hp = hp

  @property
  def name (self):
    '''Access the name attribute'''
    return self._name

  @property
  def hp (self):
    '''Accesss the hp attribute'''
    return self._hp

  def take_damage(self, dmg):
    '''Takes the dmg as the input. Applies the damage to the hp. If the hp goes below 0 then the hp is set to 0. Returns nothing.'''
    self._hp -= dmg
    if (self._hp < 0):
      self._hp = 0

  def __str__ (self):
    '''Takes no input. Uses the name, hp, and original hp in order to display information for the string. Returns the string.'''
    return f'{self._name}: {self._hp}/{self._og_hp}'

  @abc.abstractmethod
  def melee_attack (self, entity):
    '''The attack one entity does to another.'''
    pass

