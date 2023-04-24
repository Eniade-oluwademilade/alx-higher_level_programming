#!/usr/bin/python3
"""Append string to text file"""


def write_file(filename="", text=""):
    """Function adds a string to file and returns the number of characters"""
    with open(filename, "a" encoding="utf-8") as f:
        return f.write(text)
