#import the necessary modules
import functions
from exceptions import PasswordLengthError, LessThanOne


if __name__ == '__main__':
    
    # create a loop to catch exceptions until you get a character length that's satisfactory
    while True:
        # if successful, it'll break the while loop
        try:
            length = int(input("How many characters for your password? "))

            # calls the lengthCheck function which can raise the PasswordLengthError created in the exceptions module
            functions.lengthCheck(length)
            break

        # catches the PasswordLengthError, but loops the code back once it executes this code as we need a password length
        except PasswordLengthError as e:
            print(e)

        # catches a ValueError, but loops the code back once it executes this code as we need a password length
        except ValueError:
            print("Please input a number.\n")
    
    # just so it looks pretty
    print("")

    # another try/catch, but this time we try to catch a LessThanOne error created in the exceptions module
    try:
        amount = int(input("How many passwords? "))
        if amount <= 0:
            raise LessThanOne
    
    # catches the LessThanOne error, but this time sets a default of three passwords
    except LessThanOne:
        print("You've entered a number less than one. Setting the default to 3 passwords....\n")
        amount = 3
    
    # catches a ValueError, but this time sets a default of three passwords
    except ValueError:
        print("You've entered a non-number. Setting the default to 3 passwords....\n")
        amount = 3
    
    # just so it looks pretty
    print("")

    # call the generate function in the functions module and store it in a list here
    passwordList = functions.generate(length, amount)

    print("Here are your generated passwords:\n--------------")
    # print the passwords
    for password in passwordList:
        print(password)
    
    print("")




