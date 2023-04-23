from Entities import entity
import random

class Hero (entity.Entity):
  '''Represents the player otherwise known as the hero
  Attributes:
    name (str) - the player's name
    hp (int) - the player's hitpoints'''
  def __init__(self, name):
    self._health_potions = 3
    self._mana_potions = 2
    self._mp = 40
    self._og_mp = self._mp
    super().__init__(name, 25)
    
  @property
  def health_potions(self):
    '''Access the health potion attribute in main.'''
    return self._health_potions

  @property
  def mana_potions(self):
    '''Access the mana potion attribute in main.'''
    return self._mana_potions

  @property
  def mp (self):
    '''Access the mp attribute in main.'''
    return self._mp

  @property
  def og_mp (self):
    '''Access the initial mp attribute in main.'''
    return self._og_mp

  def melee_attack(self, entity):
    '''Takes an input of whatever the player is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(2, 6) + random.randint(2, 6)
    entity.take_damage(dmg)
    return f'{self._name} slashes the {entity._name} for {dmg} damage.'

  def range_attack(self, entity):
    '''Takes an input of whatever the player is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    dmg = random.randint(1, 12)
    entity.take_damage(dmg)
    return f'{self._name} pierces the {entity._name} for {dmg} damage.'

  def magic_type(self, type, entity, list_of_entities):
    '''Takes an input of the type of magic (int), the entity you want to attack (obj), and the list of current enemies (list of obj). Selects the type of magic the user has picked and applies attack. Returns description of event.'''
    if (type == 1):
      return self._magic_strike(entity)
    else:
      return self._magic_wave(list_of_entities)

  def _magic_strike(self, entity):
    '''Takes an input of whatever the player is attacking. Calculates the damage and then applies it to the opponents hp. Returns a string describing the process.'''
    self._mp -= 10
    dmg = random.randint(6, 10)
    entity.take_damage(dmg)
    return f'{self._name} casts a powerful spell on the {entity._name} and does {dmg} damage.'

  def _magic_wave(self, list_of_entities):
    '''Takes an input of whatever the player is attacking. Calculates the damage and then applies it to all opponents hp. Returns a string describing the process.'''
    self._mp -= 20
    for opp in list_of_entities:
      dmg = random.randint(4, 8)
      opp.take_damage(dmg)
    return f'{self._name} summons a massive wave that damages all enemies!'

  def use_potion(self, type):
    '''Takes an input of the type of potion the player wants to use. Selects the potion type and calls the appropriate method. Returns description of event.'''
    if (type == 1):
      return self._use_health_potion()
    else:
      return self._use_mana_potion()
    
  def _use_health_potion (self):
    '''Takes no input. Applies hp boost to player. Returns description of event.'''
    if (self._hp == self._og_hp):
      return f'{self._name} has full health!'
    self._health_potions -= 1
    self._hp += 10
    if (self._hp > self._og_hp):
      self._hp = self._og_hp
    return f'{self._name} uses a health potion! {self._name} now has {self._hp} hp!'

  def _use_mana_potion (self):
    '''Takes no input. Applies mp boost to player. Returns description of event.'''
    if (self._mp == self._og_mp):
      return f'{self._name} has full mana!'
    self._mana_potions -= 1
    self._mp += 10
    if (self._mp > self._og_mp):
      self._mp = self._og_mp
    return f'{self._name} uses a mana potion! {self._name} now has {self._mp} mp!'

  def __str__ (self):
    '''Takes no input. Uses the name, hp, and original hp in order to display information for the string. Returns the string.'''
    return f'{self._name}: \nHP: {self._hp}/{self._og_hp}\nMP: {self._mp}/{self._og_mp}\nHealth Potions: {self._health_potions}\nMana Potions: {self._mana_potions}'