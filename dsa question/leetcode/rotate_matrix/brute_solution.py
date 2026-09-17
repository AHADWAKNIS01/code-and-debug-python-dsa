# Description:
# Rotate a matrix 90 degrees clockwise.
# Each element is directly placed at its rotated position.
#
# Time Complexity (TC): O(R * C)
# Space Complexity (SC): O(R * C)

def rotate_matrix(matrix):
    r = len(matrix)
    c = len(matrix[0])

    # Create result matrix
    transpose = [[0 for _ in range(r)] for _ in range(c)]

    # Place elements at their rotated positions
    for i in range(r):
        for j in range(c):
            transpose[j][r - 1 - i] = matrix[i][j]

    return transpose


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_matrix(matrix))

# Output:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]