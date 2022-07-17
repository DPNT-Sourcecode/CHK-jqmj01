def compute(x: int, y: int) -> int:
    '''Sum two numbers
    
    Args: 
        x: a positive integer between 0-100
        y: a positive integer between 0-100

    Returns: 
        int: an integer representing the sum of the two numbers
    '''

    if(x < 0 or x > 100):
        raise ValueError("num1 must be in the range 0-100")
    if(y < 0 or y > 100):
        raise ValueError("num2 must be in the range 0-100")
    
    return x + y

