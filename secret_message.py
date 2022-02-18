'''
Created on Feb 16, 2022

@author: ctate
'''

if __name__ == '__main__':
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?/\\[]{};':\"-=_+`~!@#$%^&*()\|ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?/\\[]{};':\"-=_+`~!@#$%^&*()\|"
    stringToEncrypt = input("Please enter a message to encrypt: ")
    stringToEncrypt = stringToEncrypt.upper()
    shiftAmount = input("Please enter a whole number from 1-25 to be your key. ")
    while not shiftAmount.isnumeric() or int(shiftAmount) < 0 or int(shiftAmount) > 25:
        shiftAmount = input("Please try again and enter a whole number from 1-25 to be your key. ")
    shiftAmount = int(shiftAmount)
    encryptedString = ""
    for currentCharacter in stringToEncrypt:
        position = alphabet.find(currentCharacter)
        newPosition = position + shiftAmount
        encryptedString = encryptedString + alphabet[newPosition]
    print("Your encrypted message is: ", encryptedString)