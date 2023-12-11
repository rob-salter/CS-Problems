import math
from itertools import combinations_with_replacement

def triplets_with_sum(number):
    combinations = combinations_with_replacement(range(int(number / 2)),2)
    return [[n[0], n[1], int(math.sqrt(n[0]**2 + n[1]**2))] for n in combinations if (n[0] + n[1] + math.sqrt(n[0]**2 + n[1]**2)) == number]    
