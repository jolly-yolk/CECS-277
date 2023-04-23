from Entities import entity
import random

class EasyWizard(entity.Entity):
  def __init__ (self):
    '''Represents an easy wizard
  Attributes:
    name (str) - the wizard's prefered name
    hp (int) - wizard's hit points'''
    super().__init__('Incompetent Wizard', random.randint(7, 9))

  def melee_attack(self, entity):
    '''Takes an input of whatever the wizard is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(4, 7)
    entity.take_damage(dmg)
    return f'{self._name} zaps {entity._name} for {dmg} damage.'