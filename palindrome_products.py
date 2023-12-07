from itertools import combinations_with_replacement

# def is_palindrome(number):
#     return str(number) == str(number)[::-1]

def palindrome(min_factor, max_factor, smallest=True):
    if min_factor > max_factor:
        raise ValueError("Incorrect inputs.")
    args = (min_factor**2, max_factor**2+1) if smallest else (max_factor**2, min_factor**2-1, -1)
    for i in range(*args):
        s = str(i)
        if s == s[::-1]:
            if factors(min_factor, max_factor, i):
                return (i, factors(min_factor, max_factor, i))     

    # combinations = combinations_with_replacement(range(*args), 2)
    # for c in combinations:
    #     if str(c[0] * c[1]) == str(c[0] * c[1])[::-1]:
    #         return c[0] * c[1]
    # return [(c[0] * c[1]) for c in combinations if str(c[0] * c[1]) == str(c[0] * c[1])[::-1]]   
    
       
# def factors(min_factor, max_factor, value):
#     return [[i[0],i[1]] for i in combinations_with_replacement(range(min_factor, max_factor+1),2) if i[0] * i[1] ==  value]
           
def factors(min_factor, max_factor, value):
    return [[i,j] for i in range(min_factor, max_factor+1) for j in range(min_factor, max_factor+1) if i * j ==  value and min_factor <= i <= j <= max_factor]

def largest(min_factor, max_factor):
    if not palindrome(min_factor, max_factor, smallest=False):
        return None, []
    return palindrome(min_factor, max_factor, smallest=False)  
    # if not max_pdrome:
    #     return None, []
    # # max_pdrome = max(palindromes)
    # return max_pdrome, factors(min_factor, max_factor, max_pdrome)
    
    
def smallest(min_factor, max_factor):
    if not palindrome(min_factor, max_factor):
        return None, []
    return palindrome(min_factor, max_factor) 
    # min_pdrome = palindrome(min_factor, max_factor)
    # if not min_pdrome:
    #     return None, []
    # # min_pdrome = min(palindromes)
    # return min_pdrome, factors(min_factor, max_factor, min_pdrome)


# print(smallest(10,99))
# print(largest(10,99))
# print(factors(1,101,101))
print(palindrome(100,999, smallest=False))