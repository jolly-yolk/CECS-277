from Entities import entity
import random

class Troll(entity.Entity):
  '''Represents an easy Troll
  Attributes:
    name (str) - the troll's prefered name
    hp (int) - troll's hit points'''
  def __init__ (self):
    super().__init__('Troll', random.randint(6, 10))

  def melee_attack(self, entity):
    '''Takes an input of whatever the troll is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(5, 8)
    entity.take_damage(dmg)
    return f'{self._name} slams {entity._name} for {dmg} damage.'