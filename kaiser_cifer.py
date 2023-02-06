#!/bin/python3

# date created: 06/02/2023
# last modified: 06/02/2023
# author: flooijdt
# description: encrypt and decrypt text using
# ceasar cipher.

option = input("Do you want to (e)ncrypt or (d)ecrypt?")

key = input("Please enter the key (0 to 25) to use.")

message = input("Enter the message to encrypt.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ciphered = ""
if option == "e":
    for char in message:
        if char == " ":
            ciphered += " "
        else:
            ciphered += alphabet[alphabet.index(char) + int(key)]
elif option == "d":
    for char in message:
        if char == " ":
            ciphered += " "
        else:
            alphabet[alphabet.index(char) - int(key)]
else:
    print("you entered an invalid option.")

print(ciphered.upper())