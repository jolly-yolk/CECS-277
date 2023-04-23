#Name: Joshua Correa, Nathan Heidari
#Date: 02/21/23
#Description: Too bogged down with work? So much so that you can't even keep track of it? Well then do I have a program for you! Try out our new task keeper! Pens and paper are out; bits and bytes are in! The only limit to our program is what you do!
from task import Task
import check_input

def read_file(filename):
  '''Input is the name of the file which is always tasklist.txt. The output is a list of task objects that were created from each line of the txt file. Index 0 is the description, Index 1 is the date, and Index 2 is the time. Since the txt file seperates all the attributes with commas we split each element of the current list where we see a comma.'''
  file = open(filename)
  lines = file.read().splitlines() #creates a list of each line WITHOUT NEW LINE
  tasklist = []
  for line in lines:
    line = line.split(',') #splits the current line of the txt file into a list of the description, date, time.
    i = Task(line[0], line[1], line[2])
    tasklist.append(i) #puts the current task object in the list.
  file.close()
  return tasklist
  
def write_file(filename, tasklist):
  '''The input is the filename which is always tasklist.txt and the list of task objects. There is no output but the function does write all list of tasks onto the txt file. This function completely rewrites the tasklist.txt file so whater initial came into this program is either rewritten or was removed in the main menu function.'''
  file = open(filename, 'w')
  i = 0
  for line in tasklist:
    if (i != len(tasklist) - 1): #checks for end of list
      file.write(repr(line) + '\n') #writes the repr of the Task object into the file
      i += 1
    else: #once you reach the end of the list you don't add a new line
      file.write(repr(line)) #writes the repr of the Task object into the fil
  file.close()

def get_date():
    '''This function takes no input. The output of this function is the date that the task (whatever it may be) needs to be completed. The function prompts the user 3 times to pick relevant dates and then formats it to fit the rest of the tasks. '''
    year = check_input.get_int_range('Enter Year: ', 2000, 3000)
    month = check_input.get_int_range('Enter Month: ', 1, 12)
    day = check_input.get_int_range('Enter Day: ', 1, 31)
    if (month < 10):
        month = "0{}".format(month)
    if (day < 10):
        day = "0{}".format(day)
    return "{}/{}/{}".format(year, month, day)

def get_time():
    '''The function takes no input. The output is the time formatted how it would be in the txt file. We prompt the user twice and then format their answer.'''
    hour = check_input.get_int_range('Enter Hour: ',0,23)
    minute = check_input.get_int_range('Enter Minute: ',0,59)
    if (hour < 10):
      hour = "0{}".format(minute)
    if (minute < 10):
      minute = "0{}".format(minute)
    return "{}:{}".format(hour, minute)
  
def main_menu():
  '''This is the function that calls all other functions and serves as the backbone of the entire program.'''
  tasklist = read_file('tasklist.txt')
  while True:
    print("-Tasklist-")

    tasklist.sort() #sorts the list from recent tasks to future tasks
    if (len(tasklist) > 0): #if anything in list
      current_task = tasklist[0] #current task is the first in the list after sorting
        
    print(f'Tasks to complete: {len(tasklist)}')
    print('1. Display current task')
    print('2. Mark current task complete')
    print('3. Postpone current task')
    print('4. Add new task')
    print('5. Save and quit')
    choice = check_input.get_int_range("Enter choice: ", 1, 5)
    
    if (choice == 1):
      if (len(tasklist) == 0):
        print('All tasks are complete. Way to go!')
      else:
        print('Current task is:')
        print(current_task)
      
    elif (choice == 2):
      if (len(tasklist) == 0):
        print('All tasks are complete. Way to go!')
      else:
        print('Marking current task as complete:')
        print(current_task)
      
        tasklist.remove(current_task)
        if (len(tasklist) > 0):  
          print('New current task is:')
          current_task = tasklist[0]
          print(current_task)
        else:
          print('Nothing more to do! You just can\'t be beat!')
        
    elif (choice == 3):
      if (len(tasklist) == 0):
        print('All tasks are complete. Way to go!')
      else:
        print('Postponing task:')
        print(current_task)
      
        print('Enter new due date:')
        new_date = get_date()
        print('Enter new time:')
        new_time = get_time()
        current_task.date = new_date
        current_task.time = new_time
      
        print(current_task)
        print()
      
    elif (choice == 4):
      desc = input('Enter a task: ')
      print('Enter a due date:')
      date = get_date()
      print('Enter time: ')
      time = get_time()
      tasklist.append(Task(desc, date, time))
      
    elif (choice == 5): 
      write_file('tasklist.txt', tasklist)
      break
  
main_menu()