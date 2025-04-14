#!/usr/bin/python3
"""
This module is documented
"""


def text_indentation(text):
    """
    Indents text
    """
    if not isinstance(text, str) or text == "":
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in '.?:':
            print("\n")
            while i + 1 < length and text[i + 1] == " ":
                i += 1
        i += 1
