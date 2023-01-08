#!/usr/bin/python3

def no_c(my_string):
     copy_my_string = [letter for letter in my_string if letter != 'c' and
             letter != 'C']
    return (copy_my_string)
