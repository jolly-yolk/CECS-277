from Factories import enemy_factory
import random
from Entities import master_goblin
from Entities import master_ogre
from Entities import master_troll
from Entities import master_wizard

class MasterFactory(enemy_factory.EnemyFactory):
  '''Represents a factory that creates expert enemies'''
  def create_random_enemy (self):
    poss_enemies = [master_goblin.MasterGoblin(), master_troll.MasterTroll(), master_ogre.MasterOgre(), master_wizard.MasterWizard()]
    return random.choice(poss_enemies)