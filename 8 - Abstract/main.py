import fire
import grass
import water
import random
import check_input
import pokemon_list
#Name: Joshua Correa, Nathan Heidari
#Date: 3/14/23
#Description: Do you miss your childhood pokemon card game? Or afraid that your too old to play with those old expensive bendable cards? Fear not this program allows you to play the same pokemon game but without using the pokemon cards and with the annoying kids! This program allows you to have fun and enjoy the same pokemon game that you used play as a kid and have an more interactive program that you can constantly play with everytime!

def main():
  '''The Main program allows the user to choose a single pokemon among of the three types fire, water,and water from this the user is able to choose what type of attack they would like to call on while displaying the resulting string, The Gym Leader pokemon would be chosen at random along with his randomn type and move to attack. The following attack with each other will last until the either pokemon is defeated by hp reaching 0 and displaying an winner/loser message  '''
  weather = 1  #randomly chooses a weather multiplier
  gym_leader_type = random.randint(0, 2) #randomly chooses the type of gym leader you will fight
  hard = False #if the player chooses hard mode
  opp_pokemon = [] #list of all opponent pokemon
  player_pokemon = [] #list of all player pokemon
  line = '' #line that is spoken to indicate weather
  if (gym_leader_type == 0): #Fire
    for name in pokemon_list.fire: #appends 3 fire pokemon to opponent pokemon list
      x = random.choice(pokemon_list.fire)
      if (fire.Fire(x) not in opp_pokemon):
        if (len(opp_pokemon) < 3):
          opp_pokemon.append(fire.Fire(x))
        else:
          break
    gym_leader_type = 'FIRE' #sets the gym leader type to a string that is used to tell the player what they are up against
    
  elif (gym_leader_type == 1): #Water
    for name in pokemon_list.water: #appends 3 water pokemon to opponent pokemon list
      x = random.choice(pokemon_list.water)
      if (water.Water(x) not in opp_pokemon):
        if (len(opp_pokemon) < 3):
          opp_pokemon.append(water.Water(x))
        else:
          break
    gym_leader_type = 'WATER'
    
  elif (gym_leader_type == 2): #grass
    for name in pokemon_list.grass: #appends 3 grass pokemon to opponent the list
      x = random.choice(pokemon_list.grass)
      if (grass.Grass(x) not in opp_pokemon):
        if (len(opp_pokemon) < 3):
          opp_pokemon.append(grass.Grass(x))
        else:
          break
    gym_leader_type = 'GRASS'
    
  print(f'PROF OAK: Hello Trainer! Today you\'re off to fight \nyour first gym battle of 1 vs. 3 {gym_leader_type} pokemon. \nSelect the pokemon that you will fight with.')
  print('1. I choose you, Charmander.\n2. Squirtle! GO!\n3. We can do it, Bulbasaur!\n4. Come on Professor Oak I want a real challenge!')
  player_type = check_input.get_int_range('Please choose a pokemon (or try hard mode...): ', 1, 4) #player is able to chooses what pokemon they want to fight

  if (player_type == 1): #Fire Type
    player_pokemon.append(fire.Fire('Charmander')) #appends the players pokemon choice
    
  elif (player_type == 2): #Water Type
    player_pokemon.append(water.Water('Squirtle'))
    
  elif (player_type == 3): #Grass Type
    player_pokemon.append(grass.Grass('Bulbasaur'))
    
  elif (player_type == 4): #Hard Mode
    print()
    hard = True 
    opp_pokemon = [] #empties opponent pokemon list to prepare for exactly 9 pokemon
    print('PROF OAK: A real challenge? Okay if you say so...')
    for i in range(len(pokemon_list.fire)): #these for loops append 3 of each type of pokemon 3 * 3 = 9
      x = random.choice(pokemon_list.fire)
      if (fire.Fire(x) not in opp_pokemon):
        if (len(opp_pokemon) < 3):
          opp_pokemon.append(fire.Fire(x))  
      else:
        break
        
    for name in pokemon_list.water:
      x = random.choice(pokemon_list.water)
      if (water.Water(x) not in opp_pokemon):
        if (len(opp_pokemon) < 6):
          opp_pokemon.append(water.Water(x))
        else:
          break
          
    for name in pokemon_list.grass:
      x = random.choice(pokemon_list.grass)
      if (grass.Grass(x) not in opp_pokemon):
        if (len(opp_pokemon) < 9):
          opp_pokemon.append(grass.Grass(x))
        else:
          break
          
    player_pokemon.append(fire.Fire('Charmander')) #append each pokemon that the player could've chose (3)
    player_pokemon.append(water.Water('Squirtle'))
    player_pokemon.append(grass.Grass('Bulbasaur'))
    print()
    print('GYM LEADER: You want to fight a 3 vs. 9? It\'s your funeral!')
  random.shuffle(opp_pokemon) #shuffle the opponent pokemon list to make player think about effectiveness in each battle

  if (weather == 0): #checks wheather condition to output a line indicating weather
    line = 'GYM LEADER: Damn. Its so HOT out here. Oh well, won\'t stop me from beating you!'
    
  elif (weather == 1):
    for pokemon in opp_pokemon:
      if (isinstance(pokemon, water.Water)):
        line = f'GYM LEADER: RAIN? Heh. A perfect condition for my {pokemon.name}... '
        break
    if (len(line) == 0):
      line = 'GYM LEADER: RAIN? (i hope they don\'t have a water pokemon)'
        
  elif (weather == 2):
    line = 'PROF OAK: I\'m sure glad my PETUNIAS are getting all this SUN.'
  
  elif (weather == 3):
    line = 'PROF OAK: The weather is absolutely perfect today. Isn\'t it?'
  
  print()
  print(line)
  print()
  
  current_pokemon = 0 #current pokemon you are fighting with
  print('--GYM BATTLE--')
  while True:
    if (len(opp_pokemon) == 1): #this block of code displays how many pokemon the Gym Leader has left
      print('GYM LEADER POKEMON: ')
    else:
      print('GYM LEADER POKEMON:', end = ' ')
    for i in range(len(opp_pokemon) - 2):
      print('*', end = ' ')
    if (len(opp_pokemon) == 1):
      print('GYM LEADER: Only 1 left? Don\'t fail me now!')
    else:
      print('*')
      
    print('GYM LEADER: I choose you:')
    print(opp_pokemon[0])
    print()
    
    print(player_pokemon[current_pokemon])
    if (len(player_pokemon) == 1):
      print('Choose an Attack Type:\n1. Normal\n2. Special')
      type = check_input.get_int_range('Enter attack type: ', 1, 2) #makes the player choose an attack type
    else:
      print('Choose an Attack Type or Change Pokemon:\n1. Normal\n2. Special\n3. Change pokemon')
      type = check_input.get_int_range('Enter attack type or pokemon: ', 1, 3) #makes the player choose an attack type or change pokemon
    print()
    
    if (type == 1): #displays generic pokemon attack menu
      print(player_pokemon[current_pokemon].get_normal_menu())
    elif (type == 2): #displays unique pokemon special attack menu
      print(player_pokemon[current_pokemon].get_special_menu())
    elif (type == 3): #displays pokemon that player can choose
      for i in range(len(player_pokemon)):
        print(f'{i + 1}. {str(player_pokemon[i])}')
      current_pokemon = check_input.get_int_range('Which pokemon do you want?: ', 1, len(player_pokemon))
      current_pokemon -= 1
      print()
      print(f'{player_pokemon[current_pokemon].name} I choose you!')
      print()
      continue
      
    if (type != 3): #if you didn't change pokemon you can attack
      move = check_input.get_int_range('Enter move: ', 1, 2) #makes the user choose a move
      print()
    
      print(player_pokemon[current_pokemon].attack(opp_pokemon[0], type, move, weather)) #calls the player's attack and prints the player's attack

    if (opp_pokemon[0].hp == 0): #hp of opponent pokemon reach 0
      print('GYM LEADER: NOOOOOO! You defeated my pokemon!')
      print()
      opp_pokemon.remove(opp_pokemon[0]) #removes opponent pokemon from list 
      if (len(opp_pokemon) == 0): #if no enemy pokemon left you win
        break
      continue
      
    opp_type = random.randint(1, 2) #random opponent type
    opp_move = random.randint(1, 2) #random opponent move
    print(opp_pokemon[0].attack(player_pokemon[current_pokemon], opp_type, opp_move, weather)) #calls the opponent's attack and prints the opponent's attack
    
    if (player_pokemon[current_pokemon].hp == 0):  #User Pokemon reaches hp of 0, displayes loser message
      name = str(player_pokemon[current_pokemon]).split(':')
      print(f'{name[0]} has fallen...')
      player_pokemon.remove(player_pokemon[current_pokemon])
      current_pokemon = 0
      if (len(player_pokemon) == 0): #if the player has no pokemon left
        if (hard == True):
          print('GYM LEADER: Was that a real enough challenge?')
        else:
          print('GYM LEADER: You should\'ve trained harder...')
        print()
        break
    print()
      
  if (len(player_pokemon) != 0) and (hard == False): #If user pokemon's hp not 0 then prints Winner message
    print('YOU WON! You defeated the gym leader.')
  elif (len(player_pokemon) != 0) and (hard == True):
    print('YOU WON! You must be a pokemon master!')
  elif (len(player_pokemon) == 0) and (hard == True):
    print('YOU LOSE! Maybe try an easier mode?')
  else:
    print('YOU LOSE! Better luck next time!')

main()