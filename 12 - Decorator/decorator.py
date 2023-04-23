import abc
import monster

class Decorator(monster.Monster, abc.ABC):
  '''Represents: An abstract decorator class.
  Attributes:
    monst (Monster) - The monster object passed in the __init__
  The Decorator class abstracts and extends from the Monster'''
  def __init__(self, monst):
    super().__init__(monst._name, monst._hp)
    self._monst = monst

  def attack(self):
    '''Calls the attack on the monster attributes'''
    return self._monst.attack()
    