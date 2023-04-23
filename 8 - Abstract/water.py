import pokemon
import random

class Water(pokemon.Pokemon):
  """Represents a water type pokemon
     Attributes:
      same as pokemon but has an input for the name. The type is set to 1."""
  def __init__(self, name):
    '''Calls super to set the name and type of pokemon.'''
    super().__init__(name, type = 1)

  def get_special_menu (self):
    '''Returns which move would be used on the special menu. This method is abstract.'''
    return 'Choose a Move:\n1. Water Gun\n2. Bubble Beam'
  
  def _special_move (self, opponent, move, weather):
    '''returns the type of move that would attack opponent. This method is abstract.'''
    if (move == 1):
      return self._water_gun(opponent, weather)
    elif (move == 2):
      return self._bubble_beam(opponent, weather)

  def _water_gun(self, opponent, weather):
    '''Water Gun damages the opponent. Returns string description of the attack on the opponent. '''
    dmg = random.randint(3, 10) #Random damage 

    if (weather == 1):
      dmg *= 1.25
      if (type(dmg) == float):
        dmg = int(round(dmg))
        
    eff = self._battle_table[self._type][opponent._type]
    
    if (eff == 2):
      dmg *= 2
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a WATER GUN for {dmg} damage.\nIt was SUPER EFFECTIVE!'
      
    elif (eff == .5):
      dmg *= .5
      if (type(dmg) == float):
        dmg = int(round(dmg))
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a WATER GUN for {dmg} damage.\nIt was not very effective.'

    elif (eff == 1):
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a WATER GUN for {dmg} damage.'

  def _bubble_beam(self, opponent, weather):
    '''bubble beam damages opponent. Returns string description of the attack on the opponent.'''
    dmg = random.randint(4, 9)

    if (weather == 1):
      dmg *= 1.25
      if (type(dmg) == float):
        dmg = int(round(dmg))
        
    eff = self._battle_table[self._type][opponent._type]
    
    if (eff == 2):
      dmg *= 2
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {dmg} damage.\nIt was SUPER EFFECTIVE!'
      
    elif (eff == .5):
      dmg *= .5
      if (type(dmg) == float):
        dmg = int(round(dmg))
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {dmg} damage.\nIt was not very effective.'

    elif (eff == 1):
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a BUBBLE BEAM for {dmg} damage.'