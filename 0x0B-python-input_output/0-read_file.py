 #!/usr/bin/python3
 
"""Reads a text file (UTF8) and prints it to stdout
Args:
    filename: the file to read
"""
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(f.read, end="")
