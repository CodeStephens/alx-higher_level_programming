#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tup_a_list = list(tuple_a)
        tup_a_list[1] = 0
    if len*tuple_b) < 2:
        tup_b_list = list(tuple_b)
        tup_b_list[1] = 0
    new_tuple = []
    for i in range(2):
        new_tuple[i] = tup_a_list[i] + tup_b_list[i]
    new_tuple_tuple = tuple(new_tuple)
