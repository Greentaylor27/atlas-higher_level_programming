#Function that adds two integers or floats together and returns sum
#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Conditionals for the function to make sure 
    all inputs are ints/floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """If the function passes then it should return the sum"""
    return (int(a + b))
