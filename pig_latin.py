#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: June 2021
# This program determines the smallest of 10 numbers

def main():

    ay = 'ay'
    way = 'way'
    consonant = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b',
                 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
                 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

    vowel = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')   

    user_input = input("Enter a phrase to translate: ")

    letter1 = user_input[0]
    letter1 = str(letter1)
    letter1 = letter1.upper()
    if letter1 in consonant:
        length_of_word = len(user_input)
        remove_letter1 = user_input[1:length_of_word]
        platin = remove_letter1 + letter1 + ay
        print(platin)
    elif letter1 in vowel:
        platin = user_input + way
        print(platin)
    else:
        print("Input must be a letter!")


if __name__ == "__main__":
    main()
