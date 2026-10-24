# Python Questions and Answers

Simple revision notes for Python basics, functions, exceptions, and threading. Duplicate questions have been combined into one entry.

## Table of Contents
1. Magic methods
2. Type casting
3. Mutable and immutable objects
4. Python memory management
5. Constants
6. Identity and membership operators
7. `for` and `while` loops
8. Changing strings
9. `append()` and `insert()`
10. `remove()` and `pop()`
11. Aliasing and cloning
12. Set `add()` and `update()`
13. Functions
14. Built-in functions
15. User-defined functions
16. Decorators
17. Generators
18. Exceptions
19. Exception handling
20. Purpose of exception handling
21. Processes and threads
22. `start()` and `run()`
23. `join()`
24. Daemon threads
25. Locks
26. `Lock` and `RLock`
27. Semaphores
28. `Event` and `Condition`
29. FIFO and LIFO queues
30. `queue.Queue()` and producer-consumer programs

---

## 1. What is a magic method (`__add__`)?

Magic methods are special methods whose names begin and end with double underscores. They let objects work with Python operations. `__add__()` is associated with the `+` operator.

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)
print(a + b)  # 30
```

## 2. What is type casting?

Type casting means converting a value from one data type to another. Common functions are `int()`, `float()`, `complex()`, `bool()` and `str()`.

```python
print(int("10"))   # 10
print(float(10))   # 10.0
print(str(25))     # "25"
print(bool(1))     # True
```

**Type casting** is an intentional conversion. **Type coercion** is an automatic conversion performed by Python in certain operations.

```python
print(10 + 2.5)  # 12.5; the integer is converted for this operation
```

`int()` and `float()` cannot directly convert a complex number such as `3+4j`.

## 3. What is mutable and immutable?

A **mutable** object can be changed after creation. An **immutable** object cannot be changed after creation.

```python
items = [10, 20, 30]  # list is mutable
items[0] = 100
print(items)  # [100, 20, 30]

name = "Python"       # string is immutable
new_name = name.replace("P", "J")
print(name)      # Python
print(new_name)  # Jython
```

Common mutable types: `list`, `dict`, `set`. Common immutable types: `int`, `float`, `bool`, `str`. A tuple is immutable, although it can contain references to mutable objects.

## 4. How does Python utilize memory?

Python creates objects in memory and variables refer to those objects. Python may reuse some existing objects depending on the value and implementation, and it manages objects that are no longer needed.

```python
a = [10, 20, 30]
b = a
b.append(40)
print(a)  # [10, 20, 30, 40]
```

Here, `a` and `b` refer to the same list. Python uses reference counting and garbage collection to help manage memory. Object reuse is not guaranteed for every value.

## 5. What are constants in Python? Does Python support constants?

Python has no special `const` keyword that prevents reassignment. By convention, programmers use uppercase names for values that should not change.

```python
MAX_VALUE = 100
PI = 3.14159
```

This is a convention; Python does not strictly prevent these variables from being reassigned.

## 6. What is the difference between `is`, `is not`, `in` and `not in`?

- `is`: checks whether two references point to the same object.
- `is not`: checks whether they point to different objects.
- `in`: checks whether a value is present in a collection.
- `not in`: checks whether a value is absent from a collection.

```python
a = [10, 20]
b = a
c = [10, 20]
print(a is b)       # True
print(a is c)       # False
print(10 in a)      # True
print(50 not in a)  # True
```

Use `==` and `!=` to compare values.

## 7. What is the difference between a `for` loop and a `while` loop?

A `for` loop is commonly used to iterate over items in a sequence or other iterable. A `while` loop repeats as long as its condition is true.

```python
for n in range(1, 4):
    print(n)

n = 1
while n <= 3:
    print(n)
    n += 1
```

Both examples print `1`, `2`, and `3`. Make sure a `while` loop can eventually reach a false condition.

## 8. How can we change a string if strings are immutable?

String methods such as `replace()` return a new string; they do not modify the original string.

```python
name = "Hello Python"
new_name = name.replace("Python", "World")
print(name)      # Hello Python
print(new_name)  # Hello World
```

You can assign the result back to the same variable: `name = name.replace("Python", "World")`.

## 9. What is the difference between `append()` and `insert()`?

`append()` adds an item at the end of a list. `insert()` adds an item at a specified index.

```python
items = [10, 20, 30]
items.append(40)
print(items)  # [10, 20, 30, 40]
items.insert(1, 15)
print(items)  # [10, 15, 20, 30, 40]
```

## 10. What is the difference between `remove()` and `pop()`?

| `remove()` | `pop()` |
|---|---|
| Removes by value | Removes by index |
| Returns `None` | Returns the removed item |
| Raises `ValueError` if the value is missing | Raises `IndexError` if the list is empty or the index is invalid |
| `items.remove(20)` | `items.pop(1)` |

```python
items = [10, 20, 30, 40]
items.remove(20)
print(items)  # [10, 30, 40]
removed = items.pop(1)
print(removed)  # 30
print(items)    # [10, 40]
```

Without an argument, `pop()` removes and returns the last item.

## 11. What are aliasing and cloning in a list?

**Aliasing** means two variables refer to the same list. **Cloning** means creating a separate list object.

```python
x = [10, 20, 30]
y = x
y[0] = 100
print(x)  # [100, 20, 30]
```

To make a shallow copy, use slicing or `copy()`:

```python
x = [10, 20, 30]
y = x.copy()  # Or: y = x[:]
y[0] = 100
print(x)  # [10, 20, 30]
print(y)  # [100, 20, 30]
```

A shallow copy does not copy nested mutable objects; those can still be shared.

## 12. What is the difference between `add()` and `update()` in a set?

`add()` adds one item. `update()` adds items from one or more iterable objects.

```python
numbers = {10, 20}
numbers.add(30)
numbers.update([40, 50])
print(numbers)  # Contains 10, 20, 30, 40, 50
```

Sets are unordered, so the displayed order can vary.

## 13. What is a function?

A function is a reusable block of code that performs a task.

```python
def add(a, b):
    return a + b

print(add(10, 20))  # 30
print(add(5, 7))    # 12
```

## 14. What is a built-in function?

A built-in function comes with Python and can be used without defining it yourself. Examples include `print()`, `len()`, `type()`, `sum()`, `max()` and `min()`.

```python
numbers = [10, 20, 30]
print(len(numbers))  # 3
print(sum(numbers))  # 60
```

## 15. What is a user-defined function?

A user-defined function is written by a programmer for a particular task.

```python
def greet(name):
    print("Hello", name)

greet("Amit")  # Hello Amit
```

## 16. What is a decorator?

A decorator is a function that adds to or changes the behavior of another function without changing its original code. It is often applied using `@decorator_name`.

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
```

Output:

```text
Before function
Hello!
After function
```

Decorators are commonly used for logging, authentication, timing and permission checks.

## 17. What is a generator?

A generator produces values one at a time using `yield`, rather than returning all values at once.

```python
def get_numbers():
    yield 10
    yield 20
    yield 30

for number in get_numbers():
    print(number)
```

Generators can save memory when processing large amounts of data because values are produced as needed.

## 18. What is an exception?

An exception is an error or unusual event that occurs while a program is running and interrupts its normal execution.

```python
print(10 / 0)  # Raises ZeroDivisionError
```

## 19. What is exception handling?

Exception handling is a way to respond to errors during program execution. Python provides `try`, `except`, `else` and `finally`.

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Number cannot be zero.")
finally:
    print("Program finished.")
```

- `try`: contains code that might raise an exception.
- `except`: handles a matching exception.
- `else`: runs if the `try` block has no exception.
- `finally`: normally runs whether or not an exception occurs.

## 20. What is the purpose of exception handling?

It lets a program respond to expected errors in a controlled way, show useful messages, and perform cleanup instead of stopping unexpectedly. For example, an application can tell a user that an amount is invalid instead of showing a traceback.

---

# Threading Questions

## 21. What is the difference between a process and a thread?

A **process** is a running program with its own process memory space. A **thread** is a path of execution inside a process.

| Process | Thread |
|---|---|
| Has its own process memory space | Shares process memory with other threads |
| Usually has more creation overhead | Usually has less creation overhead |
| Can communicate through pipes or queues | Can share data directly with other threads |
| Often isolated from failures in other processes | Unsafe shared-data access can affect the process |

A browser may use multiple processes, and a process may contain multiple threads.

## 22. What is the difference between `start()` and `run()`?

`start()` starts a new thread and arranges for its `run()` method to execute in that thread. Calling `run()` directly executes the method in the current thread; it does not start a new thread.

```python
from threading import Thread

def task():
    print("Task is running")

t = Thread(target=task)
t.start()
t.join()
```

## 23. Why do we use `join()`?

`join()` makes the current thread wait for another thread to finish.

```python
from threading import Thread
import time

def task():
    time.sleep(2)
    print("Task completed")

t = Thread(target=task)
t.start()
t.join()
print("Main program continues")
```

The main thread waits for `t` before printing the final message.

## 24. What is a daemon thread?

A daemon thread is a background thread that does not keep the Python process alive by itself. Python can exit when only daemon threads remain.

```python
from threading import Thread
import time

def background_task():
    while True:
        print("Background task")
        time.sleep(1)

t = Thread(target=background_task, daemon=True)
t.start()
```

Daemon threads may be stopped abruptly when the program exits. Use non-daemon threads for work that must finish cleanly.

## 25. What problem does a lock solve?

A lock helps prevent multiple threads from changing shared data at the same time in an unsafe way, helping avoid race conditions.

```python
from threading import Thread, Lock

counter = 0
lock = Lock()

def increase():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1

t1 = Thread(target=increase)
t2 = Thread(target=increase)
t1.start()
t2.start()
t1.join()
t2.join()
print(counter)  # 20000
```

## 26. What is the difference between `Lock` and `RLock`?

- `Lock` is a basic lock. A thread holding it cannot acquire it again until it releases it.
- `RLock` is reentrant: the same thread can acquire it multiple times, but must release it the same number of times.

Use `RLock` when nested code in the same thread may acquire the same lock again.

## 27. When would you use a semaphore?

A semaphore limits how many threads can access a resource at once. A semaphore with a value of `3` allows up to three threads into the protected section simultaneously.

```python
from threading import Semaphore

connection_limit = Semaphore(3)

def use_connection():
    with connection_limit:
        print("Using a connection")
        # Work with the connection here
```

Semaphores are useful for limited resources such as database connections.

## 28. What is the difference between `Event` and `Condition`?

- `Event` lets threads wait for a signal. One thread sets the event so waiting threads can continue.
- `Condition` lets threads wait until a particular condition is true. It is used with a lock and can notify waiting threads.

Event example:

```python
from threading import Event, Thread

ready = Event()

def worker():
    ready.wait()
    print("Signal received")

t = Thread(target=worker)
t.start()
ready.set()
t.join()
```

Condition example:

```python
from threading import Condition, Thread

condition = Condition()
data_ready = False

def worker():
    global data_ready
    with condition:
        condition.wait_for(lambda: data_ready)
        print("Data is ready")

t = Thread(target=worker)
t.start()

with condition:
    data_ready = True
    condition.notify_all()

t.join()
```

Use an `Event` for a shared signal and a `Condition` when threads must wait for a specific state.

## 29. What is the difference between FIFO and LIFO queues?

- **FIFO (First In, First Out):** the first item added is the first removed.
- **LIFO (Last In, First Out):** the last item added is the first removed.

```python
from queue import Queue, LifoQueue

fifo = Queue()
fifo.put(10)
fifo.put(20)
print(fifo.get())  # 10

lifo = LifoQueue()
lifo.put(10)
lifo.put(20)
print(lifo.get())  # 20
```

FIFO is like a waiting line; LIFO is like a stack of plates.

## 30. Why is `queue.Queue()` useful in producer-consumer programs?

`queue.Queue()` provides a thread-safe way for threads to exchange data. A **producer** adds items, and a **consumer** takes and processes them. The queue handles synchronization for its `put()` and `get()` operations.

```python
from queue import Queue
from threading import Thread

tasks = Queue()

def producer():
    for item in [10, 20, 30]:
        tasks.put(item)

def consumer():
    while True:
        item = tasks.get()
        try:
            if item is None:  # Stop signal
                return
            print("Processing:", item)
        finally:
            tasks.task_done()

p = Thread(target=producer)
c = Thread(target=consumer)

c.start()
p.start()
p.join()
tasks.put(None)  # Tell the consumer to stop
tasks.join()
c.join()
```

The `None` value is a sentinel telling the consumer to stop. Choose a sentinel that cannot be confused with a normal task.

---

## Quick Revision

- `__add__()` — special method associated with `+`.
- Type casting — intentionally convert one type to another.
- Mutable — can be changed after creation.
- Immutable — cannot be changed after creation.
- `is` — checks object identity; `==` checks value equality.
- `append()` — adds at the end; `insert()` adds at an index.
- `remove()` — removes by value; `pop()` removes by index and returns the item.
- Aliasing — variables refer to the same object; cloning creates a separate copy.
- Function — reusable block of code.
- Decorator — wraps a function to extend its behavior.
- Generator — produces values one at a time using `yield`.
- Exception handling — responds to runtime errors.
- `start()` — starts a new thread; `join()` waits for a thread to finish.
- Lock — protects shared data from unsafe concurrent access.
- Semaphore — limits simultaneous access.
- Event — signals waiting threads; Condition — coordinates around a condition.
- `queue.Queue()` — safely exchanges data between threads.