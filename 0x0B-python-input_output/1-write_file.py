#!/usr/bin/python3
""" Defines a text file-writing function"""


def write_file(filename="", text=""):
    """writes text content to a filename of a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
