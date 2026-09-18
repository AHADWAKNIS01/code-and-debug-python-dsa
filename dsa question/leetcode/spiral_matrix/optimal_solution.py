def spiral_matrix(matrix):
    left=0
    top=0
    r=len(matrix)
    c=len(matrix[0])

    bottom=r-1
    right=c-1


   
   
    while top <= bottom and left <= right:

        for i in range(left,right):
            print(matrix[top][i])


        top+=1

        for i in range(top,bottom):
            print(matrix[i][right])
            right+=1

        bottom+=1
        for i in range(right,left):
            print(matrix[bottom][i])


        bottom-=1


        for i in range(bottom,top):
            print(matrix[i][left])


        left+=1

        

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

spiral_matrix(matrix)

# Output:
# 1 2 3 6 9 8 7 4 5