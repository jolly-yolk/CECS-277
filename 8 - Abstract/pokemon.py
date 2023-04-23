import random
import abc

class Pokemon (abc.ABC):
  """Represents a generic pokemon that all types of pokemon hail from.
     Attributes:
      _name (str) - the name of the pokemon
      _type (int) - the type of pokemon (fire = 0, water = 1, grass = 2)
      _hp (int) - the health of the pokemon
      _battle_table (list) - a 2D list that tells whether or not an attack is effective against an opponent, based on type.
      """
  def __init__(self, name, type):
    '''Sets the name and type of Pokemon along with assigning hp and battle table list'''
    self._name = name
    self._type = type
    self._hp = 25 
    self._battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]
    
  @property
  def hp(self):
    '''Access the health property in main.'''
    return self._hp

  @property
  def name (self):
    '''Access the name property in main'''
    return self._name
  
  def get_normal_menu (self):
    ''' Returns a string with Menu Options'''
    return "Choose a Move:\n1. Slam\n2. Tackle"
    
  def _normal_move (self, opponent, move):
    '''Uses the moving parameter to call on slam or tackle method which returns the string from those methods '''
    if (move == 1):
      return self._slam(opponent,move)
      
    elif (move == 2):
      return self._tackle(opponent)
      
  def _slam (self, opponent, move):
    '''Randomize damages on opponent and returns the string description on the move with pokemon name and type of move along with damage taken'''
    dmg = random.randint(1, 6)
    opponent._take_damage(dmg)
    return f'{self._name} SLAMS {opponent._name} for {dmg} damage.'
    
  def _tackle (self, opponent):
    '''Returns the amout of damage taken on the opponent'''
    dmg = random.randint(2, 5)
    opponent._take_damage(dmg)
    return f'{self._name} TACKLES {opponent._name} for {dmg} damage.'

  @abc.abstractmethod
  def get_special_menu (self):
    """Showing special method for specific type. Abstract method will be overrided by type class (i.e. fire, grass, water)."""
    pass

  @abc.abstractmethod
  def _special_move (self, opponent, move, weather):
    """Moves the parameter to call on either of the special moves for the type. Abstract method will be overrided by type class (i.e. fire, grass, water)."""
    pass

  def attack (self, opponent, type, move, weather):
    '''Calls either to use special move or normal moves'''
    if (type == 1):
      return self._normal_move(opponent, move)
      
    elif (type == 2):
      return self._special_move(opponent, move, weather)

  def __str__ (self):
    '''returns pokemon name and hp as string'''
    return f'{self._name}: {self._hp}/25'

  def _take_damage (self, dmg):
    '''Subtracts the dmg value from pokemon hp so that it can display the damage on the pokemon takes'''
    self._hp -= dmg
    if (self._hp < 0): #if health is negative set to 0
      self._hp = 0