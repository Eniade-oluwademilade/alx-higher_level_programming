#!/usr/bin/python3
"""Function reads file to stdout"""

def read_file(filename=""):
    """Reads file to stdout
       filename: name of file to print to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
