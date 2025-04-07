### Cheatsheet: Control Flow Tips & Tricks

### Quick Rules

- Always end `if`, `for`, `while`, etc., with a colon `:`
- Code blocks under control flow need **indentation**
- Boolean logic: `and`, `or`, `not`

### Shorthand if/else (Ternary)

```python
x = 5
y = "Big" if x > 3 else "Small"

```

### Loop with index

```python
for i, value in enumerate(["a", "b", "c"]):
    print(i, value)

```

### Loop over dictionary

```python
info = {"name": "Neo", "role": "Hacker"}
for key, value in info.items():
    print(key, value)

```

### Infinite loop trick

```python
while True:
    # do stuff
    if condition:
        break

```

### else with loops (rarely used, but cool)

```python
for i in range(5):
    if i == 7:
        break
else:
    print("Loop completed without break")

```

---
