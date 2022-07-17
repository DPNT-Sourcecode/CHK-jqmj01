def sum_two_numbers(num1: int, num2: int) -> int:
    '''Sum two numbers
    
    Args: 
        num1: a positive integer between 0-100
        num2: a positive integer between 0-100

    Returns: 
        int: an integer representing the sum of the two numbers
    '''

    if(num1 < 0 or num1 > 100):
        raise ValueError("num1 must be in the range 0-100")
    if(num2 < 0 or num2 > 100):
        raise ValueError("num2 must be in the range 0-100")
    
    return num1 + num2