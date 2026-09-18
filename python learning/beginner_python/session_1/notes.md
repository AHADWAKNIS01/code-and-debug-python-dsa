# Python Session 01

## Variables, Data Types & Print Statements

### 1. What is Python?

* High-level, general-purpose programming language.
* Created by **Guido van Rossum**.
* First released in **1991**.
* Easy syntax, dynamically typed, versatile.
* Used in **Web Development, AI/ML, Data Science, Automation, Data Engineering, Cybersecurity**.

---

### 2. Variables

A variable is a **name that refers to a value**.

```python
name = "Ahad"
age = 19
```

Python automatically determines the data type.

### Naming Rules

✅ Start with letter or `_`
✅ Can contain letters, numbers, `_`
❌ Cannot start with a number
❌ Cannot use keywords (`if`, `for`, `while`)
✅ Case-sensitive: `age`, `Age`, `AGE` are different.

**Best practice:**

```python
student_name = "Ahad"
```

---

### 3. Basic Data Types

| Type    | Example   | Meaning        |
| ------- | --------- | -------------- |
| `int`   | `10`      | Whole number   |
| `float` | `3.14`    | Decimal number |
| `str`   | `"Hello"` | Text           |
| `bool`  | `True`    | True/False     |

Check type:

```python
type(10)        # int
type(3.14)      # float
type("Hello")   # str
type(True)      # bool
```

---

### 4. `print()`

Used to display output.

```python
print("Hello")
print(10)
```

### `sep`

Controls the separator between values.

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

### `end`

Controls what comes at the end.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

---

### 5. F-Strings

Used to insert variables inside strings.

```python
name = "Ahad"
age = 19

print(f"My name is {name} and I am {age}.")
```

---

### 6. Type Conversion

**Implicit:** Python converts automatically.

```python
10 + 2.5   # 12.5
```

**Explicit:** Programmer converts manually.

```python
int("10")
float("10")
str(10)
bool(1)
```

---

### 7. `input()`

Used to take input from the user.

```python
name = input("Enter name: ")
```

⚠️ **Important:** `input()` always returns a **string**.

For integer:

```python
age = int(input("Enter age: "))
```

For float:

```python
price = float(input("Enter price: "))
```

---

## ⭐ Quick Revision

```text
Python → Programming Language

Variable → Name referring to a value

int     → Whole number
float   → Decimal
str     → Text
bool    → True/False

print() → Output
input() → User input
type()  → Check data type

sep     → Separator between values
end     → What comes after print

int()   → Convert to integer
float() → Convert to float
str()   → Convert to string
bool()  → Convert to Boolean

f"..."  → F-string
```

### Remember

```text
input() → always gives str
```

If you need a number:

```python
num = int(input("Enter number: "))
```
