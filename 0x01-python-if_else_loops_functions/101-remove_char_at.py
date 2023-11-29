#!/usr/bin/python3
def remove_char_at(input_str, index):
    # Check if index is a valid position
    if 0 <= index < len(input_str):
        result_str = ""
        
        # Copy characters up to the specified index
        for i in range(index):
            result_str += input_str[i]

        # Copy characters after the specified index
        for i in range(index + 1, len(input_str)):
            result_str += input_str[i]

        return result_str
    else:
        # Return the original string if index is out of bounds
        return input_str

