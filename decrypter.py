import sys, select, os

#print intro
print('''Welcome to Caesar Cipher Decrypter.''')

#ask user the message
message = input('Enter the message you want to decrypt: ')

#symbols 
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'

#Loop over every possible key length
for key in range(len(SYMBOLS)):
    translated = ''

    #loop symbol over message to check messages
    for symbol in message:

        if symbol in SYMBOLS:

            num = SYMBOLS.find(symbol) #fiding symbol positions
            num = num - key #decrypt the number

            if num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        
        else:
            translated = translated + symbol

    #Print key position and the decrypted message:
    print(f'key {key} decrypted value is {translated}')