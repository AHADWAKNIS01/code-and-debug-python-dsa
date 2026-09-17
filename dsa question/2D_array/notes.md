# DSA — 2D Lists / Matrices

## 1. What is a 2D List?

A **2D list** is a list containing other lists. It is commonly used to represent a **matrix**.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

* Rows = `3`
* Columns = `3`
* Elements = `9`

```text
      0   1   2
   ┌─────────────
0  │ 1   2   3
1  │ 4   5   6
2  │ 7   8   9
```

---

## 2. Accessing Elements

### Syntax

```python
matrix[row][column]
```

Example:

```python
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6
print(matrix[2][1])  # 8
```

**Remember:** `[row][column]`

---

## 3. Rows & Columns

```python
rows = len(matrix)
cols = len(matrix[0])
```

For a rectangular matrix:

```text
Rows    → len(matrix)
Columns → len(matrix[0])
```

---

## 4. Matrix Traversal

The most important pattern is **nested loops**.

```python
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j])
```

* `i` → row
* `j` → column

### Basic Template ⭐

```python
for i in range(rows):
    for j in range(cols):
        # matrix[i][j]
```

---

## 5. Row-wise Traversal

Process one complete row at a time.

```python
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

---

## 6. Column-wise Traversal

Process one complete column at a time.

```python
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()
```

Output:

```text
1 4 7
2 5 8
3 6 9
```

### Remember

```text
Row-wise    → i outer, j inner
Column-wise → j outer, i inner
```

---

## 7. Main Diagonal

For a square matrix:

```text
1 2 3
4 5 6
7 8 9
```

Main diagonal:

```text
1
  5
    9
```

### Condition

```python
i == j
```

Example:

```python
for i in range(rows):
    for j in range(cols):
        if i == j:
            print(matrix[i][j])
```

---

## 8. Upper & Lower Triangle

### Upper Triangle

```text
1 2 3
  5 6
    9
```

Condition:

```python
i <= j
```

### Lower Triangle

```text
1
4 5
7 8 9
```

Condition:

```python
i >= j
```

### ⭐ Remember

```text
Main diagonal  → i == j
Upper triangle → i <= j
Lower triangle → i >= j
```

---

## 9. Transpose

Transpose changes **rows into columns** and **columns into rows**.

Original:

```text
1 2 3
4 5 6
```

Transpose:

```text
1 4
2 5
3 6
```

### Formula

```python
transpose[j][i] = matrix[i][j]
```

### Code

```python
rows = len(matrix)
cols = len(matrix[0])

transpose = [[0] * rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]
```

---

## 10. Creating a 2D List

### General Pattern ⭐

```python
matrix = [[0] * cols for _ in range(rows)]
```

Example:

```python
matrix = [[0] * 4 for _ in range(3)]
```

Creates:

```text
0 0 0 0
0 0 0 0
0 0 0 0
```

### ⚠️ Important

Prefer:

```python
[[0] * cols for _ in range(rows)]
```

Avoid:

```python
[[0] * cols] * rows
```

The second approach creates multiple references to the **same inner list**, which can cause unexpected changes.

---

# 11. Time & Space Complexity

For a matrix with `R` rows and `C` columns:

### Traversal

```python
for i in range(R):
    for j in range(C):
```

**Time Complexity:**

```text
O(R × C)
```

Every element is visited once.

**Space Complexity:**

```text
O(1)
```

If no extra matrix is created.

If an additional `R × C` matrix is created:

```text
O(R × C)
```

---

# ⭐ DSA Cheat Sheet

```python
# Number of rows
rows = len(matrix)

# Number of columns
cols = len(matrix[0])

# Access
matrix[i][j]

# Row-wise
for i in range(rows):
    for j in range(cols):
        matrix[i][j]

# Column-wise
for j in range(cols):
    for i in range(rows):
        matrix[i][j]

# Main diagonal
i == j

# Upper triangle
i <= j

# Lower triangle
i >= j

# Create matrix
[[0] * cols for _ in range(rows)]

# Transpose
transpose[j][i] = matrix[i][j]
```

---

# 🎯 Practice Order

Practice these in this order:

1. Print a matrix
2. Row-wise traversal
3. Column-wise traversal
4. Main diagonal
5. Upper triangle
6. Lower triangle
7. Search an element
8. Find maximum/minimum
9. Transpose
10. Rotate matrix 90°
11. Spiral traversal
12. Set Matrix Zeroes

### Core Pattern to Memorize

```text
2D Matrix
    ↓
Rows × Columns
    ↓
matrix[i][j]
    ↓
Nested Loops
    ↓
Most Matrix DSA Problems
```
