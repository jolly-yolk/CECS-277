import pokemon
import random

class Grass (pokemon.Pokemon):
  """Represents a grass type pokemon
     Attributes:
      same as pokemon but has an input for the name. The type is set to 2."""
  def __init__(self, name):
    '''Calls super to set the name and type of pokemon.'''
    super().__init__(name, type = 2)

  
  def get_special_menu (self):
    '''Returns a special move menu. This method is abstract.'''
    return 'Choose a Move:\n1. Razor Leaf\n2. Solar Beam'

  
  def _special_move (self, opponent, move, weather):
    '''Returns the type of move that would attack opponent. This method is abstract.'''
    if (move == 1):
      return self._razor_leaf(opponent, weather)
      
    elif (move == 2):
      return self._solar_beam(opponent, weather)

  def _razor_leaf(self, opponent, weather):
    '''Razor leaf damages opponent and returns string description of the attack.'''
    dmg = random.randint(3, 10) #Radom damage range

    if (weather == 2):
      dmg *= 1.25
      if (type(dmg) == float):
        dmg = int(round(dmg))
    
    eff = self._battle_table[self._type][opponent._type]
    
    if (eff == 2):
      dmg *= 2
      opponent._take_damage(dmg)
      return f'{self._name} slices {opponent._name} with a RAZOR LEAF for {dmg} damage.\nIt was SUPER EFFECTIVE!'
      
    elif (eff == .5):
      dmg *= .5
      if (type(dmg) == float):
        dmg = int(round(dmg))
      opponent._take_damage(dmg)
      return f'{self._name} slices {opponent._name} with a RAZOR LEAF for {dmg} damage.\nIt was not very effective.'

    elif (eff == 1):
      opponent._take_damage(dmg)
      return f'{self._name} slices {opponent._name} with a RAZOR LEAF for {dmg} damage.'

  
  def _solar_beam(self, opponent, weather):
    '''solar beam move that damages opponent and returns string description of the attack on opponent.'''
    dmg = random.randint(4, 9)

    if (weather == 2):
      dmg *= 1.25
      if (type(dmg) == float):
        dmg = int(round(dmg))
    
    eff = self._battle_table[self._type][opponent._type]
    
    if (eff == 2):
      dmg *= 2
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a SOLAR BEAM for {dmg} damage.\nIt was SUPER EFFECTIVE!'
      
    elif (eff == .5):
      dmg *= .5
      if (type(dmg) == float):
        dmg = int(round(dmg))
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a SOLAR BEAM for {dmg} damage.\nIt was not very effective.'

    elif (eff == 1):
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a SOLAR BEAM for {dmg} damage.'