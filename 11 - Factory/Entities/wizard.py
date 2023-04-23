from Entities import entity
import random

class Wizard(entity.Entity):
  def __init__ (self):
    '''Represents a wizard
  Attributes:
    name (str) - the wizard's prefered name
    hp (int) - wizard's hit points'''
    super().__init__('Wizard', random.randint(9, 11))

  def melee_attack(self, entity):
    '''Takes an input of whatever the wizard is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(6, 8)
    entity.take_damage(dmg)
    return f'{self._name} blasts {entity._name} for {dmg} damage.'