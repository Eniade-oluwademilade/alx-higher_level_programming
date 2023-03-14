#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    for i in (len(new_string) - 1):
        if new_string[i] != 'c' or 'C':
            return new_string
