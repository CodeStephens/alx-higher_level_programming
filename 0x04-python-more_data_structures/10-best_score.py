#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    indeX = list(a_dictionary.keys())[0]
    temp = a_dictionary[ret]
    for i, v in a_dictionary.items():
        if v > temp:
            temp = v
            indeX = i
    return (indeX)
