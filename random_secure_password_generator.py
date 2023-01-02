"""
This script creates a secure random password with a desired quantity of letters, numbers, and symbols
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Get inputs
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Create empty lists
letterlist = []
numberlist = []
symbollist = []

#Choose random letters
lettercounter = 1
while lettercounter <= nr_letters:
  letterrand = str(letters[random.randint(0,25)])
  letterlist.append(letterrand)
  lettercounter += 1

#Choose random numbers
numbercounter = 1
while numbercounter <= nr_numbers:
  numberrand = str(numbers[random.randint(0,9)])
  numberlist.append(numberrand)
  numbercounter += 1

#Choose random sybols
symbolcounter = 1
while symbolcounter <= nr_symbols:
  symbolrand = str(symbols[random.randint(0,8)])
  symbollist.append(symbolrand)
  symbolcounter += 1

#Create master list of characters
totallen = nr_letters + nr_symbols + nr_numbers
allchars = letterlist + numberlist + symbollist

#Create blank final password string
password = ""

#Scramble characters randomly and create password
while len(password) < totallen:
  dice = random.randint(0,(len(allchars)-1))
  newchar = allchars[dice]
  allchars.remove(allchars[dice])
  password = password + newchar

#Print password
print(f"OK, {password} would be a good password")