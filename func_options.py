# Boris V
'''module from the chainsaw record holder to verify user's input''''
import re

# This function returns the user input, boolean. It can be used for the while True loops.
def user_input_yes_no():
    user_input = str(input()).lower() # Covert the user input to all lower cases.
    if user_input == 'yes' or user_input == 'y':
         return True
    else: return False

def get_input_alpha():
    ''' re.match(), get alpha only. '''
    user_input = ''
    while True:
        user_input = input()
        if user_input == "": break
        elif user_input.isdigit():
            print("No numbers, try again?")
            continue

        # TODO find a re.. to allow space as valid for entering the full name.
        # For now the str.replace() was the solution. Only creates a copy of
        # user_input that is why it won't change the value.
        replaced = user_input.replace(' ', 'a')

        # type(bool)=> value. The re.match checks for letters only, if the v replaced contains only letters, it will be a True statement.
        if re.match('[a-zA-Z]*$', replaced):
            return user_input
        else: print("No special chars, try again?")

    return None

def get_int():
    while True:
        try:
            int_numb = int(input())
            return int_numb
        except:
            print("Looking for integers, try again: ")
