import monster

class Alien (monster.Monster):
  '''The alien class introduces and extends the Alien monster name and the designated hp'''
  def __init__ (self):
    super().__init__('Alien', 5)

  def attack(self):
    '''The alien class attack level returns its added attack level which returns the attack base power of the monster'''
    return 3