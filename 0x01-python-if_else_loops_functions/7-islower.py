#!/usr/bin/python3

def islower(c):
    # Check if the ASCII value of the character is within the lowercase range
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False