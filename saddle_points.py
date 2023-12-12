def saddle_points(matrix):
    saddle_points = []

    if len(set(map(len, matrix))) > 1:
        raise ValueError("Matrix rows are not the same length.")    
    
    for row_ind,row in enumerate(matrix):
        for col_ind, number in enumerate(row):
            if number == max(row) and number == min([row[col_ind] for row in matrix]):
                saddle_points.append({"row": row_ind+1, "column": col_ind+1})      
    return saddle_points

