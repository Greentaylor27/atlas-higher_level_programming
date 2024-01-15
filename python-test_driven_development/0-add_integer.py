#Function that adds two integers or floats together and returns sum
#!/usr/bin/python3
def add_integer(a, b=98):
    """Conditionals for the function to make sure all inputs are ints/floats"""
    if isinstance(a, float):
        a = int(a)
    elif isinstance(a, int):
        a = a
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, float):
        b = int(b)
    elif isinstance(b, int):
        b = b
    else:
        raise TypeError("b must be an integer")
    """If the function passes then it should return the sum"""
    return (int(a + b))
