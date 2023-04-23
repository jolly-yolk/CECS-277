import check_input
from Concrete_Monsters import alien
from Concrete_Monsters import beast
from Concrete_Monsters import undead 
from Ability_Decorator import fire
from Ability_Decorator import flying
from Ability_Decorator import laser
from Ability_Decorator import poison

#Name: Joshua Correa, Nathan Heidari
#Date: 4/1/23
#Description: In this program the user is able to create their dream monster in a press of a button! In addition, the user will be able to decide to choice to create an moster that is either an Alien, Beast, or Undead. From these three monster the user would also be able to have attack ability attached to there monster while also having the option to even stack the abilities! Once the user is done there monster creation would be displayed along with the name and hp/attack levels.

def main():
    '''The main presents the user a menu to choose there monster from this it displays the base states of the monster they picked. Then promits the user to enter a new ability to the monster and will keep on repeating the abilities until they choose to quit which it will then display their final monster stats(hp/attack/name)'''
    print('Monster Maker!')
    print('Choose a base monster: \n1. Alien \n2. Beast \n3. Undead')
    player_choice = check_input.get_int_range("Enter choice: ", 1, 3)
    print()
    if player_choice == 1:
      a = alien.Alien()
      print(a)
    elif player_choice == 2:
      a = beast.Beast()
      print(a)
    elif player_choice == 3:
      a = undead.Undead()
      print(a)
      
    while (True):
      print('Add an ability: \n1. Fire \n2. Flying \n3. Laser \n4. Posion \n5. Quit')
      player_choice = check_input.get_int_range("Enter ability: ", 1, 5)
      print()
      if player_choice == 1:
        a = fire.Fire(a)
        print(a)
        
      elif player_choice == 2:
        a = flying.Flying(a)
        print(a)
  
      elif player_choice == 3:
        a = laser.Laser(a)
        print(a)
  
      elif player_choice == 4:
        a = poison.Poison(a)
        print(a)
  
      elif player_choice == 5:
          print('Your final monster is:')
          print(a)
          break
      
main()