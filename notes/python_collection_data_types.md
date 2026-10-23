
# Python Collection and Binary Data Types

## Table of Contents

1. List
2. Tuple
3. Set
4. Bytes
5. Bytearray
6. Dictionary
7. Frozenset
8. List vs Tuple
9. List vs Bytes vs Bytearray
10. Set vs Frozenset vs Dictionary

---

## 1. List

A list stores multiple values in a single variable.
- Lists preserve insertion order.
- Duplicate values are allowed.
- Different data types can be stored in the same list.
- Lists are mutable, so elements can be changed.
- Lists can grow or shrink dynamically.
- Lists use square brackets `[]`.
- Elements can be accessed using indexes and slices.

### Example

```python
items = [10, 20, "Python", True, 20]

print(items[0])     # 10
print(items[1:3])   # [20, 'Python']

items[0] = 100
items.append("Django")
print(items)
```

**Use case:** Storing student marks, shopping items, or a list of names.

---

## 2. Tuple

A tuple stores multiple values in an ordered collection.
- Tuples preserve insertion order.
- Duplicate values are allowed.
- Different data types can be stored together.
- Tuples are immutable, so their elements cannot be reassigned.
- Tuples commonly use parentheses `()`.
- Elements can be accessed using indexes and slices.
- A single-element tuple requires a comma, such as `(10,)`.

### Example

```python
student = (101, "Asha", 85.5, "Python")

print(student[0])  # 101
print(student[1])  # Asha

# student[0] = 102  # TypeError
```

**Use case:** Storing fixed values such as coordinates or a fixed set of record fields.

---

## 3. Set

A set stores unique elements.
- Duplicate elements are automatically removed.
- Sets are mutable.
- Elements can be added using `add()`.
- Elements can be removed using `remove()` or `discard()`.
- Sets do not support indexing or slicing.
- Set elements must be hashable.
- Use `set()` to create an empty set; `{}` creates an empty dictionary.

### Example

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)  # Contains 10, 20, and 30

numbers.add(40)
numbers.discard(20)

print(numbers)
print(30 in numbers)  # True
```

**Use case:** Maintaining unique usernames, tags, or categories.

---

## 4. Bytes

`bytes` represents an immutable sequence of byte values.
- Each element must be an integer from 0 to 255.
- Bytes objects are immutable.
- Their elements cannot be changed after creation.
- Bytes support indexing and slicing.
- They are useful for binary data and network communication.
- Bytes can be created using `bytes()`.
- A bytes literal can be written as `b"ABC"`.

### Example

```python
values = [65, 66, 67]
data = bytes(values)

print(data)       # b'ABC'
print(data[0])    # 65

# data[0] = 90    # TypeError
```

**Use case:** Working with binary data that should not be modified in place.

---

## 5. Bytearray

`bytearray` is a mutable sequence of byte values.
- Each element must be an integer from 0 to 255.
- Unlike `bytes`, a bytearray can be modified.
- Elements can be changed using indexes.
- New byte values can be added using `append()`.
- It supports indexing and slicing.
- It is useful when binary data needs editing.
- It can be created using `bytearray()`.

### Example

```python
values = [65, 66, 67]
data = bytearray(values)

print(data)  # bytearray(b'ABC')

data[0] = 90
data.append(68)

print(data)  # bytearray(b'ZBCD')
```

**Use case:** Modifying binary data in memory.

---

## 6. Dictionary (`dict`)

A dictionary stores information as key-value pairs.
- Dictionaries are mutable.
- Keys must be unique and hashable.
- Values can be duplicated.
- Keys are used to access their associated values.
- Assigning a value to an existing key replaces its previous value.
- Dictionaries preserve insertion order in Python 3.7 and later.
- Dictionaries use `{key: value}` syntax.

### Example

```python
student = {
    101: "Asha",
    102: "Ravi",
    103: "Meera"
}

print(student[101])  # Asha

student[102] = "Ravi Kumar"
student[104] = "Ishaan"

print(student)
```

### Duplicate keys

```python
data = {"name": "Ravi", "name": "Asha"}

print(data)  # {'name': 'Asha'}
```

The last value assigned to a repeated key is retained.

**Use case:** Storing student IDs and names, product details, or user profiles.

---

## 7. Frozenset

A frozenset is an immutable version of a set.
- It stores unique elements.
- Duplicate values are removed.
- Its elements cannot be added or removed after creation.
- It does not support indexing or slicing.
- It supports set operations such as union and intersection.
- It is created using `frozenset()`.
- It can be used as a dictionary key if its elements satisfy the hashability requirements.

### Example

```python
values = frozenset([10, 20, 30, 20])

print(values)
print(20 in values)  # True

other = frozenset([30, 40])

print(values | other)  # Union
print(values & other)  # Intersection

# values.add(50)  # AttributeError
```

**Use case:** Keeping a collection of unique values unchanged.

---

## 8. List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[10, 20]` | `(10, 20)` |
| Mutable | Yes | No |
| Order preserved | Yes | Yes |
| Duplicates allowed | Yes | Yes |
| Indexing supported | Yes | Yes |
| Slicing supported | Yes | Yes |
| Add or remove elements | Yes | No |
| Typical use | Changeable collections | Fixed collections |

### Example

```python
# List
colors = ["red", "green"]
colors[0] = "blue"
colors.append("yellow")

# Tuple
coordinates = (10, 20)
print(coordinates[0])

# coordinates[0] = 99  # TypeError
```

**Remember:** Use a list when values need to change. Use a tuple when the collection should remain fixed.

---

## 9. List vs Bytes vs Bytearray

| Feature | List | Bytes | Bytearray |
|---|---|---|---|
| Purpose | General collection | Binary data | Editable binary data |
| Example | `[65, 66]` | `b'AB'` | `bytearray(b'AB')` |
| Element types | Any Python objects | Integers 0–255 | Integers 0–255 |
| Mutable | Yes | No | Yes |
| Mixed data types | Allowed | Not allowed | Not allowed |
| Indexing | Supported | Supported | Supported |
| Typical use | Names, marks, objects | Immutable binary data | Mutable binary data |

### Example

```python
# List
items = [65, "B", True]
items[0] = 90

# Bytes
fixed_data = bytes([65, 66, 67])
# fixed_data[0] = 90  # TypeError

# Bytearray
editable_data = bytearray([65, 66, 67])
editable_data[0] = 90

print(items)
print(fixed_data)
print(editable_data)
```

**Remember:**
- `list`: General-purpose collection.
- `bytes`: Immutable binary data.
- `bytearray`: Mutable binary data.

---

## 10. Set vs Frozenset vs Dictionary

| Feature | Set | Frozenset | Dictionary |
|---|---|---|---|
| Stores | Unique elements | Unique elements | Key-value pairs |
| Mutable | Yes | No | Yes |
| Duplicate elements | Not allowed | Not allowed | Keys must be unique |
| Indexing | Not supported | Not supported | Values accessed by key |
| Add elements | Yes | No | Add key-value pairs |
| Remove elements | Yes | No | Yes |
| Syntax | `{10, 20}` | `frozenset([10, 20])` | `{"id": 101}` |
| Typical use | Changing unique items | Fixed unique items | Data lookup by key |

### Example

```python
# Set
skills = {"Python", "Django"}
skills.add("Angular")

# Frozenset
fixed_skills = frozenset(["Python", "Django"])

# Dictionary
student = {"id": 101, "name": "Asha"}
print(student["name"])
```

**Remember:**
- Use `set` for unique values that may change.
- Use `frozenset` for unique values that must remain unchanged.
- Use `dict` when each value needs an associated key.

---

## Quick Revision

| Data Type | Mutable? | Main Feature |
|---|---|---|
| List | Yes | Ordered collection |
| Tuple | No | Fixed ordered collection |
| Set | Yes | Unique elements |
| Bytes | No | Immutable binary data |
| Bytearray | Yes | Mutable binary data |
| Dictionary | Yes | Key-value pairs |
| Frozenset | No | Immutable set |

## Practice Questions

1. Which data type allows duplicates and supports modification?
2. What is the main difference between a list and a tuple?
3. Which data type automatically removes duplicate elements?
4. What is the difference between `bytes` and `bytearray`?
5. Which data type stores key-value pairs?
6. How do you create an empty set?
7. Can a frozenset be modified after creation?

### Answers

1. List.
2. A list is mutable; a tuple is immutable.
3. Set and frozenset.
4. Bytes is immutable; bytearray is mutable.
5. Dictionary (`dict`).
6. `set()`.
7. No.
