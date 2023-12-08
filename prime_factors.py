def factors(value):
    factors = []
    start = 2

    while value > 1:
        if value % start == 0:
            factors.append(start)
            value /= start
        else:
            start += 1
    return factors