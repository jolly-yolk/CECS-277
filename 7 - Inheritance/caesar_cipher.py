import cipher

class CaesarCipher(cipher.Cipher):
  '''
  A cipher that finds the encrypted message by looking up each letter and finding the corresponding letter in the shifted alphabet
  Attributes:
    shift (int) - initialize the alphabet and shifts the value of its number
  '''
  __doc__ = cipher.Cipher.__doc__ + __doc__
  def __init__(self, shift):
    '''Copys the init function of the Cipher class. Checks the inputted shift value to see if it is an integer.'''
    super().__init__()
    if (type(shift) == int):
      self._shift = shift
    else:
      raise TypeError('Shift must be an integer within range 0 - 25.')
    
  def _encrypt_letter(self, letter):
    '''Finds the letter in the alphabet for its location which then calculates the postion of the encrypted letter as described, which then returns the encrypted letter'''
    return self._alphabet[(self._alphabet.index(letter) + self._shift) % 26]

  def _decrypt_letter(self, letter):
    '''Finds the letter in the alphabet for its location which then calculates the postion of the decrypted letter as described, which then returns the decrypted letter'''
    return self._alphabet[(self._alphabet.index(letter) - self._shift) % 26]