import decorator

class Poison(decorator.Decorator):
  '''Poison class attached to the monster that would display the name and hp level'''
  def __init__(self, monst):
    super().__init__(monst)
    self._name = 'Poisonous ' + self._name
    self._hp += 2

  def attack(self):
    '''calls super() attack and add on additional attack power for the Poison class ability'''
    return super().attack() + 3