'''
Created on Feb 16, 2022

@author: ctate
'''

def is_negative_number_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?/\\[]{};':\"-=_+`~!@#$%^&*()\| "
    alphabet = alphabet + alphabet
    stringToEncrypt = input("Please enter a message to encrypt: ")
    stringToEncrypt = stringToEncrypt.upper()
    shiftAmount = input("Please enter a whole number from 1-25 to be your key. ")
    while not is_negative_number_digit(shiftAmount) or int(shiftAmount) < -25 or int(shiftAmount) > 25:
        shiftAmount = input("SOMETHING WENT WRONG. Please try again and enter a whole number from 1-25 to be your key. ")
    shiftAmount = int(shiftAmount)
    encryptedString = ""
    for currentCharacter in stringToEncrypt:
        if shiftAmount < 0:
            position = alphabet.find(currentCharacter, int(len(alphabet) / 2))
            newPosition = position + shiftAmount
        else:
            position = alphabet.find(currentCharacter)
            newPosition = position + shiftAmount
        encryptedString = encryptedString + alphabet[newPosition]
    print("Your encrypted message is: ", encryptedString)
