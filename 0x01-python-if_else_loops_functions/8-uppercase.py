#!/usr/bin/python3

def uppercase(input_str):
    result = ""  # Initialize an empty string to store the uppercase string
    
    for char in input_str:
        # Check if the character is a lowercase letter using ASCII values
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            # Keep non-lowercase characters unchanged
            uppercase_char = char
        
        # Append the uppercase character to the result string
        result += uppercase_char
