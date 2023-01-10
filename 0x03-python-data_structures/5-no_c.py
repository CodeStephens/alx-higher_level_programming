#!/usr/bin/python3

def no_c(my_string):
    copy_my_string = [let for let in my_string if let != 'c' and let != 'C']
    copy_my_string = ''.join(copy_my_string)
    return (copy_my_string)
