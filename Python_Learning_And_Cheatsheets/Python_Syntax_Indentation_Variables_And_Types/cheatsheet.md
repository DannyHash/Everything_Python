# Python Syntax, indentation, Variable & Types Cheat Sheet

---

## 1. Python Syntax

- **No semicolons required** (optional `;` for one-liners).
- Statements end at newline by default.
- Use `\` to split long statements.

```python
x = 10
total = x + 20 + \
        30 + 40
```

- **Comments**

```python
# Single-line comment

"""
Multi-line comment
with triple quotes
"""
```

- **Case Sensitive**

```python
Var = 5
var = 10
print(Var, var)  # 5 10
```

## 2. Python Indentation

- Mandatory (4 spaces is the standard).
- Replaces {} in other languages.

```python
if x > 0:
    print("Positive")
else:
    print("Negative")
```

- **One-liner if**

```python
if x > 0: print("Positive")
```

## 3. Python Variables

- Dynamically tiped

```python
x = 10
x = "Now I'm a string"
```

- Naming rules:

  - Start with letter or \_

  - No keywords

  - Case-sensitive

- Multiple assignments:

```python
a, b, c = 1, 2, 3
```

- Swapping variables:

```python
a, b = b, a
```

## 4. Python Data Types

| Type    | Example                   |
| ------- | ------------------------- |
| `int`   | `x = 5`                   |
| `float` | `y = 3.14`                |
| `str`   | `name = "Alice"`          |
| `bool`  | `flag = True`             |
| `list`  | `nums = [1, 2, 3]`        |
| `tuple` | `coords = (10, 20)`       |
| `dict`  | `user = {"name": "John"}` |
| `set`   | `unique = {1, 2, 3}`      |

- Check type:

```python
print(type(x))
```

- Type conversion:

```python
int("10")     # 10
str(100)      # "100"
float("5.5")  # 5.5
bool("")      # False
```

---

# Pro Tips & Tricks

---

## One-liner if-else:

```python
result = "Even" if x % 2 == 0 else "Odd"
```

## Use \_ to ignore values:

```python
for _ in range(3):
    print("Run")

x, _, y = (1, 2, 3)
```

## Dynamic variables with globals():

```python
globals()["my_var"] = 42
print(my_var)
```

## Evaluate expressions with eval():

```python
x = 10
print(eval("x + 5"))  # 15
```

## Check attributes of objects:

```python
print(dir("hello"))
```

## Use isinstance() instead of type():

```python
if isinstance(x, int):
    print("x is an int")
```

## See all local variables:

```python
print(locals())
```

---

# Useful Built-in Functions

---

| **Function**   | **Use**                              |
| -------------- | ------------------------------------ |
| `type()`       | Check the data type                  |
| `dir()`        | List attributes/methods of an object |
| `id()`         | Get the memory address of an object  |
| `isinstance()` | Perform type checking                |
| `locals()`     | Show local scope variables           |
| `globals()`    | Show global scope variables          |
