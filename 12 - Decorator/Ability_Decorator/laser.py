import decorator

class Laser(decorator.Decorator):
  '''Laser class is attached to the monster that would display the name and hp level'''
  def __init__(self, monst):
    super().__init__(monst)
    self._name = self._name + ' with Lasers'
    self._hp += 2

  def attack(self):
    '''calls super() attack and add on additional attack power for the Laser class ability'''
    return super().attack() + 4