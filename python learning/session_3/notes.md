# Python Session 03

## Conditional Statements

### 1. What is a Conditional Statement?

A conditional statement allows a program to **make decisions based on conditions**.

The condition gives either:

```text
True  → Execute the code
False → Skip / choose another block
```

---

# 2. `if` Statement

Used when you want code to execute **only when a condition is True**.

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

⚠️ **Indentation is mandatory in Python.**
Usually, use **4 spaces** inside the block.

---

# 3. `if-else` Statement

Used when there are **two possible outcomes**.

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

Only **one** of the two blocks executes.

```text
Condition True  → if block
Condition False → else block
```

---

# 4. `if-elif-else`

Used when there are **multiple conditions/outcomes**.

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")
```

### Important

Python checks conditions **from top to bottom** and executes the **first True condition**.

---

# 5. Nested `if`

An `if` statement inside another `if` statement is called a **nested if**.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

Useful when the second condition should be checked **only if the first condition is True**.

---

# 6. Ternary Operator

A simple `if-else` can be written in **one line**.

### Syntax

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

Output:

```text
Adult
```

### Example: Even/Odd

```python
num = 7

print("Even" if num % 2 == 0 else "Odd")
```

---

# ⭐ Quick Revision

```text
if
↓
Runs when condition is True

if-else
↓
Two possible outcomes

if-elif-else
↓
Multiple conditions

nested if
↓
if inside another if

ternary
↓
One-line if-else
```

### Condition Flow

```text
          Condition
          /       \
       True       False
        ↓           ↓
       if         else
```

### Important Rules

* Use `:` after `if`, `elif`, and `else`.
* Indentation is mandatory.
* `elif` means **else if**.
* Python checks `elif` conditions **top to bottom**.
* Only the **first True** condition in an `if-elif-else` chain executes.

---

# Practice Questions

### Q7

Take a number and print whether it is:

* Positive
* Negative
* Zero

### Q8

Take two numbers and print:

* Greater number
* `"Both are equal"` if they are equal.

### Q9

Take marks and print the grade:

```text
90+    → A
75–89  → B
60–74  → C
40–59  → D
< 40   → F
```

### Q10

Take a year and check whether it is a **leap year**.

A year is a leap year if:

```text
Divisible by 4
AND
Not divisible by 100
OR
Divisible by 400
```

---

# Homework

### Q11

Take age and valid ID (`True/False`).

Entry is allowed only when:

```text
age >= 18 AND valid ID
```

### Q12

Take three numbers and find the **largest** without using a built-in function.

### Q13

Using the ternary operator, print:

```text
Even
```

or

```text
Odd
```

### Q14

Calculate discount based on purchase amount:

```text
> 5000       → 20%
> 2000       → 10%
> 1000       → 5%
1000 or less → No discount
```
