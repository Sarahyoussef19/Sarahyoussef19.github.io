import random
import string

def password_generator():
    password_length = int(input('Password length (4-50): '))
    include_lowercase = input('Include lowercase letters? (y/n): ').lower()
    include_uppercase = input('Include uppercase letters? (y/n): ').lower()
    include_numbers = input('Include numbers? (y/n): ').lower()
    include_special = input('Include special characters? (y/n): ').lower()
    
    if password_length < 4 or password_length > 50:
        print('Invalid length! Please select between 4 and 50')
        return
    
    characters = '' 
    
    if include_lowercase == 'y':
        characters += string.ascii_lowercase 
    if include_uppercase == 'y':
        characters += string.ascii_uppercase 
    if include_numbers == 'y':
        characters += string.digits
    if include_special == 'y':
        characters += '!@#$%^&*'
    
    if characters == '':
        print('You must select at least one character type!')
        return
    
    password = '' 
    for i in range(password_length):
        password += random.choice(characters) 
    
    print(f'Generated password: {password}')

password_generator()