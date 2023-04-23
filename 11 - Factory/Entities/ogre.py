from Entities import entity
import random

class Ogre(entity.Entity):
  '''Represents an easy ogre
  Attributes:
    name (str) - the ogre's prefered name
    hp (int) - ogre's hit points'''
  def __init__ (self):
    super().__init__(name = 'Ogre', hp = random.randint(8, 12))

  def melee_attack(self, entity):
    '''Takes an input of whatever the ogre is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(6, 10)
    entity.take_damage(dmg)
    return f'{self._name} squeezes {entity._name} for {dmg} damage.'