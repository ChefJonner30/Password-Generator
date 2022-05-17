from calendar import c
from hashlib import new
from operator import ge
import random
import string
from re import S

from numpy import char


def generate_random_password():
    # Characters of Password
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  '!', '@', '#', '$', '%', '&', '^', '*', '(', ')']

    # Remove numbers from password
    def remove_numbers():
        characters.remove('0')
        characters.remove('1')
        characters.remove('2')
        characters.remove('3')
        characters.remove('4')
        characters.remove('5')
        characters.remove('6')
        characters.remove('7')
        characters.remove('8')
        characters.remove('9')

    # Remove special characters from password
    def remove_special_characters():
        characters.remove('!')
        characters.remove('@')
        characters.remove('#')
        characters.remove('$')
        characters.remove('%')
        characters.remove('^')
        characters.remove('&')
        characters.remove('*')
        characters.remove('(')
        characters.remove(')')

    # Input for length of password
    length = input('Please enter the length of the password: ')

    # check if length is an integer
    if length.isdigit():
        length = int(length)
    else:
        print('You did not enter a valid value, please try again.')
        generate_random_password()

    # Change content of password:
    password_type = input(
        'Would you like to have numbers as an option in the password? ').lower()
    if password_type == 'yes':
        password_type = input(
            'Great! Would you like to have special characters as an option in the password? ').lower()
        if password_type == 'yes':
            print('Great! The password is ready to be generated!')
        elif password_type == 'no':
            remove_special_characters()
            print('No Problem! The password is ready to be generated')
        elif password_type != 'yes' or password_type != 'no':
            print('You did not enter a valid answer, please try again')
            generate_random_password()
    elif password_type == 'no':
        remove_numbers()
        password_type = input(
            'No Problem! Would you like to have special characters as an option in the password? ').lower()
        if password_type == 'yes':
            print('Great! The password is ready to be generated!')
        elif password_type == 'no':
            remove_special_characters()
            print('No Problem! The password is ready to be generated')
        elif password_type != 'yes' or password_type != 'no':
            print('You did not enter a valid answer, please try again')
            generate_random_password
    elif password_type != 'yes' or password_type != 'no':
        print('You did not enter a valid answer, please try again')
        generate_random_password()

    # Shuffle the remaining characters
    random.shuffle(characters)

    # Empty Password for input
    password = []

    # Generate the random values
    for i in range(length):
        password.append(random.choice(characters))

    # Shuffle the characters appended to the password
    random.shuffle(password)

    # Convert the password to a string
    print('The password is ' + ''.join(password))

    # Generate a new password
    new_password = input('Would you like to generate a new password? ').lower()
    if new_password == 'yes':
        generate_random_password()
    else:
        print('Have a great day!')


# Call the function
generate_random_password()
