from Entities import entity
import random

class MasterWizard(entity.Entity):
  def __init__ (self):
    '''Represents a wizard
  Attributes:
    name (str) - the wizard's prefered name
    hp (int) - wizard's hit points'''
    self._used_potion = False
    super().__init__('Dark Wizard', random.randint(11, 15))

  @property
  def used_potion(self):
    return self._used_potion

  def melee_attack(self, entity):
    '''Takes an input of whatever the wizard is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(10, 15)
    entity.take_damage(dmg)
    return f'{self._name} engulfs {entity._name} in flames for {dmg} damage.'

  def use_potion(self):
    self._used_potion = True
    self._hp += 10
    if (self._hp > self._og_hp):
      self._hp = self._og_hp
    return f'{self._name} uses a potion! {self._name} now has {self._hp} hp!'