import check_input
import random
from basic_door import BasicDoor
from code_door import CodeDoor
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from locked_door import LockedDoor
#Name: Joshua Correa, Nathan Heidari
#Date: 3/21/23
#Description: Do you like escape rooms but hate how expensive it is? Do you like it so much that you wish you can play it for free with unlimited tries and in the comfort of your home? Fear not! This program allows you to participate in a simmulated Escape Room for free and inside the comfort of your home! This program prompts the user an escape room by having the user open a series of three random doors chosen from several different types of doors! These doors are a series of BasicDoor,LockedDoor,DeadboltDoor,ComboDoor, and CodeDoor. If the user is getting close to opening one of these doors the program prompts the user with a clue to help to open the door. Once the three doors are opened the User has successfully Escaped! 

def open_door(door):
  '''Passes in a door object that the user will try to unlock, while displaying description of door'''
  print(door.examine_door())
  
  while True:
    if (type(door) != ComboDoor):
      print(door.menu_option ())
      
    if (type (door) == BasicDoor):
      option = check_input.get_int_range ('Would you like to push or pull?: ', 1, door.get_menu_max ())
    elif (type (door) == CodeDoor):
      option = check_input.get_int_range ('What key would you like to press?: ', 1, door.get_menu_max ())
    elif (type (door) == ComboDoor):
      option = check_input.get_int_range (f'{door.menu_option()} ', door.get_menu_min(), door.get_menu_max ())
    elif (type (door) == DeadboltDoor):
      option = check_input.get_int_range ('Which deadbolt would you like to toggle?:  ', 1, door.get_menu_max ())
    else:
      option = check_input.get_int_range ('Where do you want to look?:  ', 1, door.get_menu_max ())
    
    print(door.attempt (option))
    if (door.is_unlocked ()):
      print(door.success ())
      break
    else:
      print(door.clue ())
      
def main():
  '''Calls the open_door function and checks to see if any doors are left. If no doors are left then the user wins. Holds a series of random doors that are going to be given to user to escape'''
  possible_doors = [BasicDoor(), CodeDoor(), ComboDoor(), DeadboltDoor(), LockedDoor()]
  doors = []
  
  while (len(doors) != 3):
    x = random.choice(possible_doors)
    if (x not in doors):
      doors.append(x)
      
  print('Welcome to the Escape Room. You must unlock 3 doors to escape...')
  print()
  
  while (len(doors) != 0):
    open_door(doors[0])
    doors.remove(doors[0])
    print()
    
  print('Congratulations! You escaped...this time.')
    
main()