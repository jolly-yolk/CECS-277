class Cipher:
  '''
  Represents a basic cipher that takes no arugments.
  Attributes:
    _alphabet (list) - a list containing all letters in the alphabet capitalized.
  '''
  def __init__(self):
    self._alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
  def encrypt_message(self, message):
    '''Takes an input of the unencrypted message. Forces the message to be capitalized. Takes each letter of the message and calls the _encrypted_letter(letter) method. Once the decrypted letter is returned it appends the letter to the encrypted message string. If the current letter is not a letter (i.e. . , ! ?) then it just appends the letter to the encrypted message string. Returns the encrypted message (str)'''
    encrypted = ''
    message = message.upper()
    for letter in message:
      if letter in self._alphabet:
        encrypted += self._encrypt_letter(letter)
      else:
        encrypted += letter
    return encrypted
    
  def decrypt_message(self, message):
    '''Takes an input of the encrypted message. Forces the message to be capitalized. Takes each letter of the message and calls the _decrypt_letter(letter) method. Once the decrypted letter is returned it appends the letter to the decrypted message string. If the current letter is not a letter (i.e. . , ! ?) then it just appends the letter to the decrypted message string. Returns the decrypted message (str).'''
    decrypted = ''
    message = message.upper()
    for letter in message:
      if letter in self._alphabet:
        decrypted += self._decrypt_letter(letter)
      else:
        decrypted += letter
    return decrypted
    
  def _encrypt_letter(self, letter):
    '''Takes the input of one letter. Encryptes the letter using the function within the square brackets. Uses the result of the function to find the atbash letter in the alphabet attribute. Returns the atbash letter.'''
    return self._alphabet[(len(self._alphabet) - 1) - self._alphabet.index(letter)]

  def _decrypt_letter(self, letter):
    '''Takes the input of one letter. Decryptes the letter using the function within the square brackets. Uses the result of the function to find the decrypted letter in the alphabet attribute. Returns the decrypted letter.'''
    return self._alphabet[(len(self._alphabet) - 1) - self._alphabet.index(letter)]