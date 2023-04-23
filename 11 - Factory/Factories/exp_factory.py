from Factories import enemy_factory
import random
from Entities import goblin
from Entities import ogre
from Entities import troll
from Entities import wizard

class ExpertFactory(enemy_factory.EnemyFactory):
  '''Represents a factory that creates expert enemies'''
  def create_random_enemy (self):
    poss_enemies = [goblin.Goblin(), troll.Troll(), ogre.Ogre(), wizard.Wizard()]
    return random.choice(poss_enemies)