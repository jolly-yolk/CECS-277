import random
from Entities import hero
import check_input
from Factories import beg_factory
from Factories import exp_factory
from Factories import mas_factory

#Name: Joshua Correa, Nathan Heidari
#Date: 4/11/23
#Description: In this program the user is set off to a journey to fight off three monsters that are obstructing his travel. From this, the three monster that he would have to fight are known to be Goblins, Ogres, and Trolls. These monsters are known to an easy fight while the others tend to be more diffcult. It is up towards the user decision to take on the challege he desires of diffculty. If the user manages to deafeat all three monsters with his special attacks and uses of potions he will successfully win and further is journey. Are you willing to take on this challenge?

def main():
  '''Takes no input. This function calls all other functions in the program and brings it all together into a cohesive execution. Returns nothing.'''
  print('Monster Trials')
  
  print() #gets the hero's name
  name = input('What is your name hero? ')
  her = hero.Hero(name)
  on = True
  
  print() #prints the objective
  print(f'You will face a series of 3 monsters, {her.name}.\nDefeat them all to continue on your journey.')
  
  print() #based on difficulty, creates an easy, medium, or hard factory to produce opponents
  diff = check_input.get_int_range('Difficulty:\n1. Beginner\n2. Expert\n3. Master\n', 1, 3)
  if (diff == 1):
    fact = beg_factory.BeginnerFactory()
  elif (diff == 2):
    fact = exp_factory.ExpertFactory()
  else:
    fact = mas_factory.MasterFactory()
    
  print() #fills the opponent list with easy, medium, or hard opponents
  opp = []
  for i in range(3):
    opp.append(fact.create_random_enemy())

  while (on == True):
    while (True):
      print(her)
      print()
      print('Choose a move:')
      print('1. Physical Attack')
      print('2. Magic Attack')
      print('3. Item')
      choice1 = check_input.get_int_range('Enter choice: ', 1, 3)
      print()
      if (choice1 == 1): #choose physical attack
        print('1. Sword Attack')
        print('2. Arrow Attack')
        print('3. Back')
        choice2 = check_input.get_int_range('Enter choice: ', 1, 3)
        print()
        if (choice2 != 3):
          print('Choose an enemy to attack:') #asks the player to choose what enemy they want to attack
          for i in range(len(opp)):
            print(f'{i + 1}. {opp[i]}')
          choice3 = check_input.get_int_range('Enter choice: ', 1, len(opp))
          print()
          choice3 -= 1
      
        if (choice2 == 1):
          print(her.melee_attack(opp[choice3]))
        elif (choice2 == 2):
          print(her.range_attack(opp[choice3]))
        else:
          continue
        
      elif (choice1 == 2): #choose magic attack
        while (True):
          print("1. Magic Strike")
          print("2. Magic Wave")
          print("3. Back")
          choice2 = check_input.get_int_range('Enter choice: ', 1, 3)
          print()
          if (choice2 == 1):
            print('Choose an enemy to attack:') #asks the player to choose what enemy they want to attack
            for i in range(len(opp)):
              print(f'{i + 1}. {opp[i]}')
            choice3 = check_input.get_int_range('Enter choice: ', 1, len(opp))
            print()
            choice3 -= 1

          if (choice2 == 2): #if you choose wave then use random opponent as argument for use_magic_type method
            choice3 = random.choice(opp)
            
          elif (choice2 == 3): #break loop and at the bottom there is a continue statement that restarts mainloop
            break

          if (her.mp == 0) or ((choice2 == 2) and (her.mp < 20)): #checks if player has enough mp
            print(f'{her.name} tries to cast a spell but nothing happens!')
            print(f'{her.name} doesn\'t have enough mp!')
            print()
            continue

          print(her.magic_type(choice2, choice3, opp))
          if (choice2 == 2): #if you use wave it shows the health of the enemies
            print()
            for i in range(len(opp)):
              print(f'{i + 1}. {opp[i]}')
            print()
          break
          
        if (choice2 == 3): #if you choose back then restart loop
          continue
          
      else: #choose use item
        while (True):
          print('1. Use a Health Potion')
          print("2. Use a Mana Potion")
          print("3. Back")
          choice2 = check_input.get_int_range('Enter choice: ', 1, 3)
          print()
          if (choice2 == 3):
            break
            
          print()
          
          if ((her.health_potions == 0) and choice2 == 1) or ((her.mana_potions == 0) and choice2 == 2): #checks if player has approapiate amount of health potions
            if (choice2 == 1):
              print(f'{her.name} has ran out of health potions!')
            else:
              print(f'{her.name} has ran out of mana potions!')
            print()
            continue
        
          print(her.use_potion(choice2))
          print()
          
        if (choice2 == 3):
          continue
        
      slain = len(opp) #this block of code checks if any of the enemies have 0 health
      for enemy in opp:    
        if (enemy.hp == 0):
          print(f'You have slain the {enemy.name}')
          opp.remove(enemy)
        
      if (len(opp) != 0): #if there is an enemy and they have 0 health they will be removed. This catches what the loop above doesn't    
        if (opp[0].hp == 0):
          print(f'You have slain the {opp[0].name}')
          opp.remove(opp[0])
    
      if (len(opp) != slain): #if an enemy has been slain check if there are any left
        print()
        if (len(opp) == 0):
          print('Congratulations! You defeated all three monsters! Your journey may continue!')
          on = False
          break
        continue
      print()
        
      if (choice1 == 2): #if you choose a magic attack
        if (choice2 == 2): #if you choose magic wave attack
          choice3 = random.randint(0, len(opp) - 1) #choose a random alive enemy to attack
        
      if (choice1 == 3): #if you used an item then you can move again
        continue
      
      elif (diff == 3) and (opp[choice3].hp < 8): #random chance for using potion once for master enemies.
        if (opp[choice3].used_potion == False):
          chance = random.randint(1, 2)
          if (chance == 1):
            print(opp[choice3].melee_attack(her))
          else:
            print(opp[choice3].use_potion())
        else:
          print(opp[choice3].melee_attack(her))
      else:
        print(opp[choice3].melee_attack(her))
      
      print() #checks if the hero's hp and the number of opponents, which are two conditions that would end the game.
      if (her.hp == 0):
        print('Your journey has come to an end...')
        on = False
        break
      
main()