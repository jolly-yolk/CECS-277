class Task:
  '''Represents a task that needs to be done with a description, time, and date.
  Attributes:
    desc (str) - description of task
    date (str) - date that the task needs to be completeted by (YYYY/MM/DD)
    time (str) - time the task needs to be completed by (HH:MM)'''
  def __init__(self, desc, date, time):
    self.desc = desc
    self.date = date
    self.time = time
    
  def get_description(self):
    '''Returns the description of the task created in the __init__.'''
    return self.desc
    
  def __str__(self):
    '''When the object is accessed, as a string would be, it returns this function.'''
    return f'{self.desc} - Due: {self.date} at {self.time}'
    
  def __repr__(self):
    '''This is the way the task is stored in tasklist.txt'''
    return f'{self.desc},{self.date},{self.time}'
    
  def __lt__(self, other):
    '''This compares an object and an other object of the same type. If the object\'s year, month, day, hour, minute, or the letter is less than the other object then the function returns True, if not it returns False.'''
    date_self = self.date.split('/')
    date_other = other.date.split('/')
    time_self = self.time.split(':')
    time_other = other.time.split(':')
    
    if (date_self[0] < date_other[0]):
      return True
    elif (date_self[0] > date_other[0]):
      return False
    elif (date_self[1] < date_other[1]):
      return True
    elif (date_self[1] > date_other[1]):
      return False
    elif (date_self[2] < date_other[2]):
      return True
    elif (date_self[2] > date_other[2]):
      return False

    elif (time_self[0] < time_other[0]):
      return True
    elif (time_self[0] > time_other[0]):
      return False
    elif (time_self[1] < time_other[1]):
      return True
    elif (time_self[1] > time_other[1]):
      return False

    word1 = []
    word2 = []
    for letter1 in self.desc:
      word1.append(letter1)
    for letter2 in other.desc:
      word2.append(letter2)

    for i in range(min(len(word1), len(word2))):
      if (word1[i] < word2[i]):
        return True
      elif (word1[i] > word2[i]):
        return False
      elif (word1[i] == word2[i]):
        continue
    return 'Its the same :P'
        
    