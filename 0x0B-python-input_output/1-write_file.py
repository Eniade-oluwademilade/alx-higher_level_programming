#!/usr/bin/python3
"""Function writes string to text file"""


def write_file(filename="", text=""):
    """Write string to file and return number of characters
        filename: name of file to write to
        text: string to write in file
    """
    with open(filename, encoding="utf-8") as f:
        return f.write(text)
