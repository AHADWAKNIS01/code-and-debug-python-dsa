def rotate_matrix(matrix):
    r=len(matrix)
    c=len(matrix[0])


    
  
    

#transpose the matrix
    for i in range(r):
        for j in range(i+1,c):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


#reverse the column
    for i in range(c):
        matrix[i].reverse()

    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_matrix(matrix))





