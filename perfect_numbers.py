def classify(number):
    """ Determine if a number is perfect by first calculating a numbers factors and
    then checking if the sum of the factors is equal to the number.

    Args:
        number ([int]): [The number from which to calculate factors and compare the sum of factors]

    Returns:
        int: A string of either perfect, abundant or deficient.
    
    Raises:
        ValueError: If arg < 1.

    """

    if number < 1:
        raise ValueError("The number should be greater than zero.")
    else:
        factors = []
        for n in range(1,number):
            if number % n == 0:
                factors.append(n)
            else:
             pass
    
        if sum(factors) == number:
            return "perfect"
        elif sum(factors) > number:
            return "abundant"
        elif sum(factors) < number:
            return "deficient"        
