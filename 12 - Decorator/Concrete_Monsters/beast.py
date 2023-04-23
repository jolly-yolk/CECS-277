import monster

class Beast(monster.Monster):
  '''The Beast class introduces and extends the Beast monster name and the designated hp'''
  def __init__(self):
    super().__init__(name = 'Beast', hp = 5)

  def attack(self):
    '''The Beast class attack level returns its added attack level which returns the attack base power of the monster'''
    return 5
    
    