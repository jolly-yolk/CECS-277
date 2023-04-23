import pokemon
import random

class Fire (pokemon.Pokemon):
  """Represents a fire type pokemon
     Attributes:
      same as pokemon but has an input for the name. The type is set to 0."""
  def __init__(self, name):
    '''Calls super to set the name and type of pokemon.'''
    super().__init__(name, type = 0)


  def get_special_menu (self):
    """Returns a string with the list of special moves. This method is abstract"""
    return 'Choose a Move:\n1. Ember\n2. Fire Blast'

  
  def _special_move (self, opponent, move, weather):
    '''Returns the type of move that would attack opponent. This method is abstract.'''
    if (move == 1):
      return self._ember(opponent, weather)
    elif (move == 2):
      return self._fire_blast(opponent, weather)

  
  def _ember(self, opponent, weather):
    '''Ember Move that damages opponent. Returns string description of the attack on the opponent.'''
    dmg = random.randint(3, 10)
    
    if (weather == 0):
      dmg *= 1.25
      if (type(dmg) == float):
        dmg = int(round(dmg))
        
    eff = self._battle_table[self._type][opponent._type] #finds eff multiplier in battle table
    
    if (eff == 2):  #Damage taken at 2
      dmg *= 2
      opponent._take_damage(dmg)
      return f'{self._name} engulfs {opponent._name} in EMBERS for {dmg} damage.\nIt was SUPER EFFECTIVE!'
      
    elif (eff == .5):  #Damage taken at.5
      dmg *= .5
      if (type(dmg) == float):
        dmg = int(round(dmg))
      opponent._take_damage(dmg)
      return f'{self._name} engulfs {opponent._name} in EMBERS for {dmg} damage.\nIt was not very effective.'

    elif (eff == 1):  #Damage taken at 1
      opponent._take_damage(dmg)
      return f'{self._name} engulfs {opponent._name} in EMBERS for {dmg} damage.'
      

  def _fire_blast(self, opponent, weather):
    '''fire blast move that damages opponent. Returns string description of the attack on the opponent.'''
    dmg = random.randint(4, 9)
    
    if (weather == 0):
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
      return f'{self._name} blasts {opponent._name} with a FIRE BLAST for {dmg} damage.\nIt was not very effective.'

    elif (eff == 1):
      opponent._take_damage(dmg)
      return f'{self._name} blasts {opponent._name} with a FIRE BLAST for {dmg} damage.'