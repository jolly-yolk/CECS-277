from Entities import entity
import random

class Goblin (entity.Entity):
  '''Represents a goblin
  Attributes:
    name (str) - the goblin's prefered name
    hp (int) - goblin's hit points'''
  def __init__ (self):
    super().__init__('Goblin', random.randint(10, 14))

  def melee_attack(self, entity):
    '''Takes an input of whatever the goblin is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(8, 12)
    entity.take_damage(dmg)
    return f'{self._name} pounces {entity._name} for {dmg} damage.'