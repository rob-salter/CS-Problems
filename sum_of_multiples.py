def sum_of_multiples(limit, multiples):
    return sum(set([i for i in range(limit) for k in multiples if k > 0 and i % k == 0])) 
