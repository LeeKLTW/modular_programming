# encoding: utf-8
import sys

def funcky_case(s):
    letters = []
    capitalize  = False
    for letter in s:
        if capitalize:
            letters.append(letter.upper())
        else:
            letters.append(letter.lower())
        capitalize = not capitalize
    return "".join(letters)
