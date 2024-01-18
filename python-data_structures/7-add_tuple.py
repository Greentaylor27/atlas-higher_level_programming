#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    max_len = max(len(tuple_a), len(tuple_b))
    tuple_a += (0,) * (max_len - len(tuple_a))
    tuple_b += (0,) * (max_len - len(tuple_b))
    
    result = tuple(a + b for a, b in zip(tuple_a, tuple_b))

    return result
