def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Sequence lengths should be the same.")
    count = 0
    for letter_a, letter_b in zip(strand_a, strand_b):
        if letter_a != letter_b:
            count +=  1
    return count
