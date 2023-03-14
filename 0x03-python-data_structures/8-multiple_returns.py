#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char_1 = sentence[0] if length > 0 else "None"
    tuple_ = length, char_1
    return (tuple_)
