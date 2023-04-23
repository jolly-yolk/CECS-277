import die

class Player:
  """Represents the player that uses the dice and checks what they have.
  Attributes:
    points (int) - your score based on your previous attempts
    dice (list) - list of the 3 dice that you have"""
  def __init__(self):
    '''Constructs and sorts list of 3 Die'''
    self.points = 0
    self.dice = [die.Die(), die.Die(), die.Die()]

  def get_points(self):
    '''returns the player points'''
    return self.points

  def roll_dice(self):
    '''Calls roll and sorts the list'''
    for i in self.dice:
      i.roll()
    self.dice.sort()

  def has_pair(self):
    '''Returns if two dice have same value'''
    if (self.dice[0] == self.dice[1]) or (self.dice[1] == self.dice[2]):
      self.points += 1    #Adds 1 point
      return True
    return False

  def has_three_of_a_kind(self):
    '''Returns if three dice have same value'''
    if (self.dice[0] == self.dice[1] == self.dice[2]):
      self.points += 3  #Adds 3 points
      return True
    return False

  def has_series(self):
    '''Returns if the dice are in a sequence'''
    if (self.dice[1] - self.dice[0] == 1) and (self.dice[2] - self.dice[1] == 1):
      self.points += 2    #Adds 2 points
      return True
    return False

  def __str__(self):
    '''returns string into proper format'''
    return f"D1={self.dice[0]} D2={self.dice[1]} D3={self.dice[2]}"
