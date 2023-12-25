from random import randint, choice
from exceptions import PasswordLengthError

# checks to see if the numbered entered is less than 8, raises an exception if it is.
def lengthCheck(num):
    if num < 8:
        raise PasswordLengthError("The password length you gave is less than 8 characters. Please try again.\n")
    else:
        return True

def passwordGenerate(length):
    # create a list of both possible characters, just special characters, and just numbers
    possibleCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "?", ",", ".", ";", ":"]
    specialCharacters = possibleCharacters[37:len(possibleCharacters) - 1]
    numbers = possibleCharacters[27:36]
    
    # final string
    returnString = ""
    
    # actual password generator
    for characterCount in range (0, length):
        # will guarantee the first character is a letter, either uppercase or lowercase
        if characterCount == 0:
            objectStored = possibleCharacters[randint(0, 26)]

            # will make sure the chance of an uppercase is random
            objectStored = choice([objectStored, objectStored.upper()])
        else:
            randNum = randint(0, len(possibleCharacters) - 1)
            objectStored = possibleCharacters[randNum]
            if randNum < 27:
                objectsStored = choice([objectStored, objectStored.upper()])
        
        returnString += objectStored
    

    # number/special character check time!!
        
    # checks to see if theres a character. otherwise, recursively calls the function to generate another password
    if any(x in returnString for x in specialCharacters):
        # checks to see if theres a number. otherwise, recursively calls the function to generate another password
        if any(y in returnString for y in specialCharacters):
            return returnString
        else:
            return passwordGenerate(length)
    else:
        return passwordGenerate(length)
        


def generate(length, amount):
    # list of what will be unique passwords
    passwordList = []

    for passwordNumber in range(0, amount):
        # generate a password
        password = passwordGenerate(length)

        # if its already in the list, it'll keep generating a password. otherwise, it'll append it to the list
        while password in passwordList:
            password = passwordGenerate(length)
            
        passwordList.append(password)
    
    return passwordList
