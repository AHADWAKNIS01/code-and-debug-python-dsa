Absolutely. Here are **Session 03 — Conditional Statements** with clean, beginner-friendly Python solutions for **Q7–Q14**, including the question, code, and short explanation.

## Session 03 — Conditional Statements

### Q7. Positive, Negative, or Zero

**Question:** Take a number as input. Print whether it is positive, negative, or zero.

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

**Logic:**

* `num > 0` → Positive
* `num < 0` → Negative
* Otherwise → Zero

---

### Q8. Greater of Two Numbers

**Question:** Take two numbers as input. Print the greater of the two. If they are equal, print `"Both are equal."`

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal.")
```

---

### Q9. Student Grade

**Question:** Take a student's marks and print their grade.

| Marks    | Grade |
| -------- | ----- |
| 90+      | A     |
| 75–89    | B     |
| 60–74    | C     |
| 40–59    | D     |
| Below 40 | F     |

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade F")
```

**Important:** We check from the **highest condition to the lowest**.

---

### Q10. Leap Year

**Question:** Check whether a year is a leap year.

A year is a leap year if:

* divisible by `400`, **OR**
* divisible by `4` but **not** divisible by `100`

```python
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")
```

**Examples:**

* `2024` → Leap year
* `1900` → Not a leap year
* `2000` → Leap year

---

# Homework

### Q11. Age and Valid ID

**Question:** A person can enter a venue only if they are **18 or older AND have a valid ID**.

```python
age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (True/False): ")

if age >= 18 and has_id == "True":
    print("You can enter the venue.")
else:
    print("You cannot enter the venue.")
```

### Logic

Both conditions must be true:

```text
age >= 18  AND  valid ID
```

If either one is false → entry denied.

---

### Q12. Largest of Three Numbers

**Question:** Take three numbers as input and print the largest without using a built-in function.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
```

**Example:**

```text
Input:
10
25
15

Output:
Largest: 25
```

**Time Complexity:** `O(1)`
Because we always perform a fixed number of comparisons.

---

### Q13. Even or Odd Using Ternary Operator

**Question:** Using the ternary operator, print `"Even"` or `"Odd"` in a single line.

```python
num = int(input("Enter a number: "))

print("Even" if num % 2 == 0 else "Odd")
```

### Normal if-else

```python
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Ternary version

```python
print("Even" if num % 2 == 0 else "Odd")
```

**Pattern:**

```python
value_if_true if condition else value_if_false
```

---

### Q14. Shop Discount

**Question:** A shop gives discounts based on purchase amount:

* Above `5000` → 20%
* Above `2000` → 10%
* Above `1000` → 5%
* `1000` or below → No discount

```python
amount = float(input("Enter purchase amount: "))

if amount > 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10
elif amount > 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final amount:", final_amount)
```

### Example

If purchase amount is `6000`:

```text
Discount = 6000 × 20 / 100
         = 1200

Final amount = 6000 - 1200
             = 4800
```

**Output:**

```text
Discount: 1200.0
Final amount: 4800.0
```

### ⭐ Important patterns to remember

```python
# if
if condition:
    statement
```

```python
# if-else
if condition:
    statement
else:
    statement
```

```python
# if-elif-else
if condition:
    statement
elif condition:
    statement
else:
    statement
```

```python
# nested if
if condition:
    if another_condition:
        statement
```

```python
# ternary
value_if_true if condition else value_if_false
```

And remember the main operators used in conditions:

`>`, `<`, `>=`, `<=`, `==`, `!=`, `and`, `or`, `not`
