def steps(number):
    steps = 0
    if number < 1:
        raise ValueError("The Collatz Conjecture is only concerned with strictly positive integers!")   

    while number != 1:
        if number % 2 == 0: 
            number = number/2
        else:
            number = (number * 3) + 1
        steps += 1
    return steps    



