
# Python Garbage Collection and Destructors

## 1. What Is Garbage Collection?

Python manages memory automatically. It has a memory-management system that reclaims memory used by objects that are no longer needed.

This process is called **Garbage Collection (GC)**.

Think of garbage collection as a cleaner that helps reclaim memory occupied by objects that are no longer in use.

### Main Objective of Garbage Collection

The main objective of garbage collection is to reclaim memory used by objects that are no longer accessible or needed.

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Shiv")

print(s1.name)

s1 = None
```

**Explanation:**

1. `Student("Shiv")` creates a `Student` object.
2. `s1` refers to that object.
3. `s1 = None` removes that reference to the object.
4. If no other references to the object exist, it becomes eligible for memory reclamation.

**Important:** In CPython, objects without remaining references are usually reclaimed immediately through reference counting. Cyclic garbage collection handles certain groups of objects that refer to one another but are otherwise unreachable.

---

## 2. When Does an Object Become Eligible for Garbage Collection?

An object generally becomes eligible for reclamation when it is no longer reachable through references from the program.

For example:

```python
class Demo:
    pass


d1 = Demo()
d2 = d1

d1 = None
```

Here, the object is **not yet eligible for reclamation**, because `d2` still refers to it.

Now execute:

```python
d2 = None
```

If no other references to the object exist, it can be reclaimed.

### Important Points

- Assigning `None` to a variable removes that variable's reference to its previous object.
- Assigning another object to a variable also replaces its previous reference.
- An object can have multiple references.
- Circular references can make objects eligible for collection even when the objects refer to one another.
- Memory reclamation timing depends on the Python implementation and the type of garbage collection involved.

---

## 3. The `gc` Module

Python provides the built-in `gc` module to inspect and control its cyclic garbage collector.

Import it using:

```python
import gc
```

### Important Functions

| Function | Purpose |
|---|---|
| `gc.isenabled()` | Returns `True` if automatic cyclic garbage collection is enabled |
| `gc.disable()` | Disables automatic cyclic garbage collection |
| `gc.enable()` | Enables automatic cyclic garbage collection |
| `gc.collect()` | Requests a garbage-collection run |

**Important:** Disabling the cyclic garbage collector does not disable all Python memory management. For example, CPython's reference counting continues to operate.

---

## 4. Check Whether Garbage Collection Is Enabled

Use `gc.isenabled()` to check whether automatic cyclic garbage collection is enabled.

```python
import gc

print(gc.isenabled())
```

**Possible output:**

```text
True
```

The exact result depends on the program's current garbage-collector configuration.

---

## 5. Disable Garbage Collection

Use `gc.disable()` to disable automatic cyclic garbage collection.

```python
import gc

print("Before:", gc.isenabled())

gc.disable()

print("After:", gc.isenabled())
```

**Output:**

```text
Before: True
After: False
```

Disabling the cyclic collector can allow unreachable reference cycles to remain in memory until collection is enabled or performed manually.

It does not mean every unused object remains in memory: reference counting in CPython can still reclaim many objects.

---

## 6. Enable Garbage Collection

Use `gc.enable()` to enable automatic cyclic garbage collection.

```python
import gc

gc.disable()
print("GC enabled:", gc.isenabled())

gc.enable()
print("GC enabled:", gc.isenabled())
```

**Output:**

```text
GC enabled: False
GC enabled: True
```

Use `gc.enable()` when you want automatic cyclic garbage collection to resume.

**Best practice:** Avoid disabling garbage collection unless you have a specific reason and understand the memory implications.

---

## 7. What Is a Destructor?

A destructor is commonly described as a special method that is called when an object is being finalized.

In Python, the method associated with this behavior is:

```python
__del__()
```

Python may call `__del__()` when an object is about to be finalized. However, its timing is not guaranteed, and it is not a reliable way to manage important resources.

### Example

```python
class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object is being finalized")


d = Demo()

d = None
```

**Possible output in CPython:**

```text
Object created
Object is being finalized
```

In this simple example, assigning `None` removes the variable's reference to the object. If no other references remain, CPython will usually finalize it promptly.

**Note:** Do not depend on the destructor running immediately or at a particular point in the program. Other Python implementations and reference cycles may behave differently.

---

## 8. What Is the Purpose of `__del__()`?

The purpose of `__del__()` is to perform finalization when an object is being finalized.

However, it is not recommended to rely on it for essential cleanup tasks such as:

- Closing database connections
- Releasing file handles
- Releasing locks
- Closing network connections

A destructor may run later than expected, may not run during interpreter shutdown in the expected way, or may interact badly with reference cycles.

### Recommended Approach: Use `with`

For files, use a context manager:

```python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

print("File operation completed")
```

The file is closed when execution leaves the `with` block, including when an exception occurs during the block.

For resources such as database connections, use the relevant library's documented context-manager or explicit cleanup mechanism.

---

## 9. Difference Between Garbage Collection and a Destructor

| Garbage Collection | Destructor (`__del__`) |
|---|---|
| A memory-management process | A special finalization method |
| Reclaims memory from eligible objects | Can run finalization code when an object is finalized |
| Managed by Python's memory-management system | Defined by the programmer when needed |
| Does not guarantee immediate cleanup for every object | Does not guarantee immediate execution |
| Can collect unreachable reference cycles | May complicate the collection of objects involved in reference cycles |

### Remember

The destructor does not directly destroy the object. It provides finalization behavior; object memory reclamation is managed by Python.

---

## 10. Quick Revision

- **Garbage Collection:** Reclaims memory used by objects that are no longer needed.
- **`gc.isenabled()`:** Checks whether automatic cyclic garbage collection is enabled.
- **`gc.disable()`:** Disables automatic cyclic garbage collection.
- **`gc.enable()`:** Enables automatic cyclic garbage collection.
- **`gc.collect()`:** Requests garbage collection.
- **`__del__()`:** A finalization method that may run when an object is being finalized.
- **`with`:** The preferred approach for managing many resources that support context managers.

---

## 11. Practice Questions

1. What is garbage collection in Python?
2. When does an object become eligible for reclamation?
3. What is the purpose of the `gc` module?
4. What does `gc.isenabled()` return?
5. What is the difference between `gc.disable()` and disabling all memory management?
6. What does `gc.collect()` do?
7. What is `__del__()`?
8. Why should we not rely on destructors to close important resources?
9. What is the difference between garbage collection and object finalization?
10. Why is the `with` statement preferred for file handling?

### Practice Program

Create a class named `Student` that:

1. Prints a message when an object is initialized.
2. Defines a `__del__()` method that prints a finalization message.
3. Creates two references to the same object.
4. Removes the first reference and observes that the object is still referenced.
5. Removes the second reference and observes the behavior in your Python implementation.

**Note:** The exact timing of the finalization message can depend on the Python implementation.
