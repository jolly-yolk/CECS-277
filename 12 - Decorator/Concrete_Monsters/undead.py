import monster

class Undead(monster.Monster):
  '''The Undead class introduces and extends the Undead monster name and the designated hp'''
  def __init__(self):
    super().__init__('Undead',7)

  def attack(self):
    '''The Undead class attack level returns its added attack level which returns the attack base power of the monster'''
    return 5
    
    