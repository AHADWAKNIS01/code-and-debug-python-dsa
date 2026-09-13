# Python Session 02

## Escape Sequences & Operators

### 1. Escape Sequences

Escape sequences start with a **backslash `\`** and are used to represent special characters inside strings.

| Escape | Meaning      | Example               |
| ------ | ------------ | --------------------- |
| `\n`   | New line     | `"Hello\nWorld"`      |
| `\t`   | Tab space    | `"Name:\tRahul"`      |
| `\\`   | Backslash    | `"C:\\Users\\Rahul"`  |
| `\"`   | Double quote | `"He said \"Hello\""` |
| `\'`   | Single quote | `'It\'s Python'`      |

Example:

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

# 2. Arithmetic Operators

Used for mathematical calculations.

| Operator | Name           |   Example |     Result |
| -------- | -------------- | --------: | ---------: |
| `+`      | Addition       |  `10 + 3` |       `13` |
| `-`      | Subtraction    |  `10 - 3` |        `7` |
| `*`      | Multiplication |  `10 * 3` |       `30` |
| `/`      | Division       |  `10 / 3` | `3.333...` |
| `//`     | Floor Division | `10 // 3` |        `3` |
| `%`      | Modulus        |  `10 % 3` |        `1` |
| `**`     | Exponentiation |  `2 ** 4` |       `16` |

### Important

```python
10 / 3    # 3.333...
10 // 3   # 3
10 % 3    # 1 → remainder
2 ** 4    # 16
```

---

# 3. Assignment Operators

Shortcuts for updating a variable.

| Operator | Same As      |
| -------- | ------------ |
| `+=`     | `x = x + n`  |
| `-=`     | `x = x - n`  |
| `*=`     | `x = x * n`  |
| `/=`     | `x = x / n`  |
| `//=`    | `x = x // n` |
| `%=`     | `x = x % n`  |
| `**=`    | `x = x ** n` |

Example:

```python
x = 10
x += 5

print(x)   # 15
```

---

# 4. Operator Precedence

When multiple operators are used, Python follows a specific order.

### Highest → Lowest

```text
**          → Exponentiation
*, /, //, % → Multiplication & Division
+, -        → Addition & Subtraction
```

Example:

```python
result = 10 + 2 * 3
```

First `2 * 3`:

```text
10 + 6 = 16
```

### Use parentheses `()` when you want to control the order.

```python
result = (10 + 2) * 3
```

Result:

```text
36
```

---

# 5. Comparison Operators

Used to compare two values.

They always return **`True` or `False`**.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

⚠️ Remember:

```text
=  → Assignment
== → Comparison
```

---

# 6. Logical Operators

Used to combine multiple conditions.

| Operator | Meaning          | True When              |
| -------- | ---------------- | ---------------------- |
| `and`    | Both conditions  | Both are `True`        |
| `or`     | Either condition | At least one is `True` |
| `not`    | Opposite         | Reverses the result    |

Examples:

```python
age = 20

print(age >= 18 and age < 60)
# True
```

```python
print(age < 18 or age >= 60)
# False
```

```python
print(not True)
# False
```

---

# 7. Other Operators

These will be covered in later sessions:

* **Identity Operators** → `is`, `is not`
* **Membership Operators** → `in`, `not in`
* **Bitwise Operators** → `&`, `|`, `^`, `~`, `<<`, `>>`

---

# ⭐ Quick Revision

```text
Escape Sequences
\n   → New line
\t   → Tab
\\   → Backslash
\"   → Double quote
\'   → Single quote

Arithmetic
+    → Add
-    → Subtract
*    → Multiply
/    → Division
//   → Floor division
%    → Remainder
**   → Power

Assignment
+=   -=   *=   /=   //=   %=   **=

Comparison
==   !=   >   <   >=   <=
          ↓
     True / False

Logical
and  → Both True
or   → At least one True
not  → Reverse result

Precedence
** → *, /, //, % → +, -
```

---

# Practice Questions

### Q1

Take two numbers and print:

* Sum
* Difference
* Product
* Remainder

### Q2

Take a number and check whether it is **even or odd** using `%`.

### Q3

Take age and check:

* Eligible to vote → `age >= 18`
* Senior citizen → `age >= 60`

### Q4

Take marks of 3 subjects and calculate:

* Total
* Average

Use an **f-string** for output.

### Homework Q5

Take a number and print:

* Number raised to power `3`
* `number // 7`
* `number % 7`

### Homework Q6

Take two numbers and calculate their product **without using `*`**, using repeated addition with `+=`.
