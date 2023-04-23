from Entities import entity
import random

class EasyOgre(entity.Entity):
  '''Represents an easy Ogre
  Attributes:
    name (str) - the ogre's prefered name
    hp (int) - ogre's hit points'''
  def __init__ (self):
    super().__init__('Senile Ogre', random.randint(7, 8))

  def melee_attack(self, entity):
    '''Takes an input of whatever the ogre is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(5, 8)
    entity.take_damage(dmg)
    return f'{self._name} smashes {entity._name} for {dmg} damage.'