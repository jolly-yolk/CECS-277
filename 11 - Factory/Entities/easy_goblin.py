from Entities import entity
import random

class EasyGoblin(entity.Entity):
  '''Represents an easy goblin
  Attributes:
    name (str) - the goblin's prefered name (it is "Goblin")
    hp (int) - goblin's hit points'''
  def __init__ (self):
    super().__init__('Feeble Goblin', random.randint(6, 9))

  def melee_attack(self, entity):
    '''Takes an input of whatever the goblin is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(5, 9)
    entity.take_damage(dmg)
    return f'{self._name} shanks {entity._name} for {dmg} damage.'
    
    
