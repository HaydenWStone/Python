"""
This scripts accepts an input and translates the message into the NATO phoentic alphabet
"""

# Define a dictionary for the NATO phonetic alphabet
nato_phonetic_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'Xray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

# Get user input
text = input("What text would you like to transcribe into the NATO alphabet? ")

# Convert input text to uppercase letters and split into a list of letters
text_list = [letter.upper() for letter in text]

# Transcribe each letter of the input text into the NATO phonetic alphabet
for letter in text_list:
    value = nato_phonetic_alphabet.get(letter, letter)
    print(value)

