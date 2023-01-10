#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        char_count = f.write(text)
    return(char_count)
