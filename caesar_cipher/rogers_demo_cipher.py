# The quick brown fox jumped over the lazy sleeping dog
# Shift of 15
# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV

#               '23',    4-> '67' 
def encrypt(plain_text, key):
  encrypted_pin = ''
  print(f'The plain text number is {plain_text}, the key is {key}.')

  for char in plain_text:
    num = int(char)
    shifted_number = num + key
    if shifted_number > 9:
      shifted_number = shifted_number % 10
    encrypted_pin += str(shifted_number)
  return encrypted_pin

def decrypt(message, key):
  return encrypt(message, -key)
  
if __name__ == "__main__":
  print(encrypt('23', 6)) # 89
  print(encrypt('23', 4)) # 67
  print(encrypt('2345', 7)) # 9012
  print(encrypt('2345', 108345345345)) # 7890
  print(decrypt('89', 6)) # 23
