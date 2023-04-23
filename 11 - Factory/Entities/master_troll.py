from Entities import entity
import random

class MasterTroll(entity.Entity):
  '''Represents an easy troll
  Attributes:
    name (str) - the troll's prefered name
    hp (int) - troll's hit points'''
  def __init__ (self):
    self._used_potion = False
    super().__init__('Menacing Troll', random.randint(12, 16))

  @property
  def used_potion(self):
    return self._used_potion

  def melee_attack(self, entity):
    '''Takes an input of whatever the troll is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(10, 14)
    entity.take_damage(dmg)
    return f'{self._name} slams {entity._name} for {dmg} damage.'

  def use_potion(self):
    self._used_potion = True
    self._hp += 10
    if (self._hp > self._og_hp):
      self._hp = self._og_hp
    return f'{self._name} uses a potion! {self._name} now has {self._hp} hp!'