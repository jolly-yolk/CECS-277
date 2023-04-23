import abc

class EnemyFactory(abc.ABC):
  '''Represents an abstract factory that all factories use as an interface'''
  @abc.abstractmethod
  def create_random_enemy (self):
    '''Abstract class that returns an entity object.'''
    pass