class Matrix:
    def __init__(self, matrix_string: str)-> list:
        """Takes a matrix string and converts to a a matrix by first splitting on \n using splitlines, a
        for loop on each row whereby we split the string so it becomes a list and then conv each
        index in the list to int."""
        
        self.matrix = [[int(x) for x in row.split()] for row in matrix_string.splitlines()]        

    def row(self, index: int) -> list:
        return self.matrix[index - 1]
        
    def column(self, index: int) -> list:
        # loop through each row of the matrix and return the chosen index
        return [row[index - 1] for row in self.matrix]

matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
print(matrix.row(1))
print(matrix.column(2))  