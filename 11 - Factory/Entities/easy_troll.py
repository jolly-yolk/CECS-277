from Entities import entity
import random

class EasyTroll(entity.Entity):
  def __init__ (self):
    '''Represents an easy Troll
  Attributes:
    name (str) - the troll's prefered name
    hp (int) - troll's hit points'''
    super().__init__('Blind Troll', random.randint(5, 7))

  def melee_attack(self, entity):
    '''Takes an input of whatever the Troll is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(4, 6)
    entity.take_damage(dmg)
    return f'{self._name} clubs {entity._name} for {dmg} damage.'