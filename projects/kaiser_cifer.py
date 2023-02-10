#!/bin/python3

# date created: 06/02/2023
# last modified: 06/02/2023
# author: flooijdt
# description: encrypt and decrypt text using
# ceasar cipher.

option = input("Do you want to (e)ncrypt or (d)ecrypt?\n")

key = int(input("Please enter the key (0 to 25) to use.\n"))

message = input("Enter the message to encrypt.\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ciphered = ""
if option == "e":
    for char in message:
        if char == " ":
            ciphered += " "
        else:
            if alphabet.index(char) + key > 25:
                indexo = alphabet.index(char) - 26 + key
                ciphered += alphabet[indexo]
            else:
                ciphered += alphabet[alphabet.index(char) + key]
elif option == "d":
    message = message.lower()
    for char in message:
        if char == " ":
            ciphered += " "
        else:
            if alphabet.index(char) - key < 0:
                indexo = alphabet.index(char) - key
                ciphered += alphabet[indexo]
            else:
                ciphered += alphabet[alphabet.index(char) - key]
else:
    print("you entered an invalid option.")

print(ciphered.upper())