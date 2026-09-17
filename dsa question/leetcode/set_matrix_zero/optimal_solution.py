# Description:
# Set the entire row and column to 0 whenever an element is 0.
# Uses separate arrays to track which rows and columns contain 0.
#
# Time Complexity (TC): O(R * C)
# Space Complexity (SC): O(R + C)

def set_zeros(matrix):
    r = len(matrix)
    c = len(matrix[0])

    rows_track = [0 for _ in range(r)]
    cols_track = [0 for _ in range(c)]

    # Track rows and columns containing 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rows_track[i] = -1
                cols_track[j] = -1

    # Set tracked rows and columns to 0
    for i in range(r):
        for j in range(c):
            if rows_track[i] == -1 or cols_track[j] == -1:
                matrix[i][j] = 0

    return matrix


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(set_zeros(matrix))

# Output:
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]