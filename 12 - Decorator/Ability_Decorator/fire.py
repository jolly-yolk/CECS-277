import decorator

class Fire(decorator.Decorator):
  '''Fire class is attached to the monster that would display the name and hp level'''
  def __init__(self, monst):
    super().__init__(monst)
    self._name = 'Fiery ' + self._name
    self._hp += 2

  def attack (self):
    '''calls super() attack and add on additional attack power for the class fire ability'''
    return super().attack() + 5