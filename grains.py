def square(number):
    if number < 1 or number > 64:
        raise ValueError("This square does not exist.")

    return 2 ** (number - 1) 
            
def total():
    return 18446744073709551615 