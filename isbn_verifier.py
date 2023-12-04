def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10 or not isbn[0:8].isdigit():
        return False
    check = 0
    for char, i in zip(isbn, range(10,0,-1)):
        if char != "X" and not char.isdigit():
            return False     
        if char == "X":
            char = 10     
        check += (int(char) * i)
        
    return check % 11 == 0