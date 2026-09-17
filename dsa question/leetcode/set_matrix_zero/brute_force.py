

def mark_infinity(matrix,rows,cols):
    r=len(matrix)
    c=len(matrix[0])

    for  i in range(0,r):
        if matrix[i][cols]!=0:
             matrix[i][cols]=float("inf")


    for j in range(0,c):
            if matrix[rows][j]!=0:
                matrix[rows][j]=float("inf")



def set_zero(matrix):
    r=len(matrix)
    c=len(matrix[0])

    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                 mark_infinity(matrix,i,j)

    for i in range(r):
            for j in range(c):
                if matrix[i][j]==float("inf"):
                     matrix[i][j]=0

    return matrix




matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(set_zero(matrix))

# Output:
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]