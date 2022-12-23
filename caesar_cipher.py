"""
This code implements a classic Caesar Cipher
By Hayden Stone
"""

#ACSII Art
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
#Intro and Get Inputs
def cipher_inputs():
    print(logo)
    print()
    print("Welcome to the Caesar Cipher")
    print()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the encryption key:\n"))
    if shift <= 0:
        shift = int(input("Sorry, please type the shift number again as a positive integer:\n"))
    cipher(direction,text,shift)

#Cipher function
def cipher(direction, text, shift):

    # Create Cipher Dictionary
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher_dict = {}
    for letter in alphabet:
        current_position = alphabet.index(letter)
        new_letter_position = (current_position + shift) % 26
        new_letter = alphabet[new_letter_position]
        cipher_dict[letter] = new_letter
    cipher_dict[" "] = " "

    # Convert message to lower case
    text = text.lower()

    # Encode mode
    if direction == "encode":
        new_text = ""
        for letter in text:
            new_letter = cipher_dict.get(letter, letter)
            new_text += new_letter

  # Decode mode
    if direction == "decode":
        new_text = ""
        for letter in text:
            for key, value in cipher_dict.items():
                if value == letter:
                    new_letter = key
                    new_text += new_letter

    # Print output
    print()
    print(f"Here's the {direction}d result:\n{new_text}")
    print()

    #Ask if the user wants to start again
    start_again = input("Would you like to start again? Type y or n\n").lower()
    print()
    if start_again == "y":
        cipher_inputs()
    else:
        print("Thank you for using the Caesar Cipher")

cipher_inputs()