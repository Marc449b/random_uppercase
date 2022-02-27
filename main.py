from random import randint
from pyperclip import copy as clipboard_copy


def generate(pre_string):
    # Initialize the string variable to be returned
    post_string = ""

    # Iterate over each letter in pre_string
    for letter in pre_string:
        # Append either uppercase or lowercase letter to post_string
        post_string += letter.upper() if randint(1, 2) == 1 else letter
    
    return post_string


if __name__ == '__main__':
    while True:
        # Prompt user to input a string, which will get randomly uppercased letters
        pre_string = input('Enter a string to get random_uppercased: ').lower()

        # Generate randomly uppercased string
        post_string = generate(pre_string)
        # Copy post_string to clipboard
        clipboard_copy(post_string)
        # Notify user, that the string has been added to clipboard
        print(f'"{post_string}" has been added to your clipboard')

        # Prompt user, if user wants to randomly uppercase another string
        if input('Do you have any other strings to get random_uppercased? (N/y): ').lower() != 'y':
            break
