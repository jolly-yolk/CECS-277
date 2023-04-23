import cipher
import caesar_cipher
import check_input
#Name: Joshua Correa, Nathan Heidari
#Date: 03/07/23
#Description: Do you have skeletons in your closet? Well you can now keep that closet locked tight with the new Secret Decoder Ring! You can choose between two different Cipher methods to encode your embarrassing secrets. Atbash or Caesar, no matter which way you encode it your secrets are fool proof!

def main():
  '''
  The main function that allows the user to interact with the cipher classes. The main function asks the user for their inputs and then creates the approiate objects based on their inputs. The main function will always open and close the message.txt file to either read or write. The main function is called once and does not contain a loop.
  '''
  print('Secret Decoder Ring:')
  print('1. Encrypy')
  print('2. Decrypt')
  crypt = check_input.get_int_range('', 1, 2)
  
  if (crypt == 1): #Encrypt asks for encryption type
    print('Enter encryption type:')
    
  else: #Decrypt asks for decryption type
    try: #trys to find the message.txt file to open. If the file does not exist then raise FileNotFoundError
      file = open("message.txt")
    except FileNotFoundError:
      raise FileNotFoundError("There is no message.txt to decrypt.")
    print('Enter decryption type:')
  print('1. Atbash')
  print('2. Caesar')
  
  type = check_input.get_int_range('', 1, 2)
  
  if (type == 2): #Caesar gets the shift value from user
    shift = check_input.get_int_range('Enter shift value: ', 0, 25)
  
  if (crypt == 1): #Encrypt prompts the user to enter a message
    message = input('Enter message: ')
    
  elif (crypt == 2): #Decrypt reads message from message.txt
    file = open('message.txt')
    message = file.read()
    file.close()
  
  if (type == 1): #Atbash this if block calls the methods for the Cipher object
    atbash = cipher.Cipher()
    
    if (crypt == 1): #Encrypt writes encrypted message on message.txt and calls the encryption method for Cipher object
      file = open('message.txt', 'w')
      file.write(atbash.encrypt_message(message))
      file.close()
      print('Encrypted message saved to "message.txt".')

    else: #Decrypt calls the decryption method for Cipher object
      print('Reading encrypted message from "message.txt".')
      print(f'Decrypted message: {atbash.decrypt_message(message)}')

  elif (type == 2): #Caesar this if block calls the methods for the CaesarCipher object
    caesar = caesar_cipher.CaesarCipher(shift)

    if (crypt == 1): #Encrypt writes encrypted message on message.txt and calls the encryption method for CaesarCipher object
      file = open('message.txt', 'w')
      file.write(caesar.encrypt_message(message))
      file.close()
      print('Encrypted message saved to "message.txt".')

    else: #Decrypt calls the decryption method for CaesarCipher object
      print('Reading encrypted message from "message.txt".')
      print(f'Decrypted message: {caesar.decrypt_message(message)}')

main()