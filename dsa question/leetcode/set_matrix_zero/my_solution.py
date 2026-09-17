def set_matrix_zero(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    zero_cols=set()
    zero_row=set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_row.add(i)
                zero_cols.add(j)
            


    for i in zero_row:
        for j in range(cols):
            matrix[i][j]=0



    for i in zero_cols:
        for j in range(rows):

            matrix[j][i]=0


    return matrix

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
print("this input is ",matrix)
print(set_matrix_zero(matrix))

# Output:
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]

            


            


            


    