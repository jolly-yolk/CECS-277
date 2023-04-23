from Factories import enemy_factory
import random
from Entities import easy_goblin
from Entities import easy_ogre
from Entities import easy_troll
from Entities import easy_wizard

class BeginnerFactory(enemy_factory.EnemyFactory):
  '''Represents a factory that creates easy enemies'''
  def create_random_enemy (self):
    poss_enemies = [easy_goblin.EasyGoblin(), easy_troll.EasyTroll(), easy_ogre.EasyOgre(), easy_wizard.EasyWizard()]
    return random.choice(poss_enemies)