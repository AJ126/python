
# Thread Synchronization in Python

## 1. What Is Synchronization?

When multiple threads access or modify shared data, their operations can interfere with each other. This may cause incorrect results or data inconsistency.

**Synchronization** coordinates access to shared resources so that operations happen safely.

Python provides synchronization tools through the `threading` module.

## 2. Lock

A `Lock` allows only one thread at a time to hold the lock.

```python
import threading

lock = threading.Lock()

def task():
    with lock:
        print("This code is protected by a lock")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
```

The `with lock:` statement acquires the lock before entering the block and releases it when the block exits, including when an exception occurs.

### `acquire()` and `release()`

```python
lock.acquire()
try:
    # Access shared data safely
    pass
finally:
    lock.release()
```

Use `try/finally` or a `with` statement to avoid leaving a lock acquired accidentally.

A standard `Lock` can be acquired by one thread and released by another; it is not an ownership-tracking lock. However, releasing an unlocked lock raises `RuntimeError`.

### Example: Protecting a Shared Counter

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for _ in range(10000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)
```

Expected output:

```text
20000
```

The lock protects the counter update from concurrent interference.

## 3. Problem With a Simple Lock

A standard `Lock` cannot be acquired again by the same thread while that thread already holds it.

If the same thread tries to acquire it again, it may block indefinitely.

This matters when a protected function calls another function that attempts to acquire the same lock.

## 4. `RLock` (Reentrant Lock)

An `RLock` allows the thread that already holds the lock to acquire it again.

The thread must release it the same number of times it acquired it before another thread can acquire it.

```python
import threading

lock = threading.RLock()

def inner():
    with lock:
        print("Inside inner function")

def outer():
    with lock:
        print("Inside outer function")
        inner()

outer()
```

Output:

```text
Inside outer function
Inside inner function
```

The same thread can enter both protected sections without blocking itself.

### Lock vs. RLock

| Lock | RLock |
|---|---|
| Cannot be acquired again by the holding thread without blocking. | Can be acquired repeatedly by its owning thread. |
| Does not track recursive acquisition depth. | Tracks the owning thread and recursion depth. |
| Suitable for simple mutual exclusion. | Useful for nested or recursive calls that acquire the same lock. |

## 5. Semaphore

A `Semaphore` limits how many threads can access a resource at the same time.

```python
import threading
import time

semaphore = threading.Semaphore(3)

def task(number):
    with semaphore:
        print(f"Task {number} entered")
        time.sleep(2)
        print(f"Task {number} leaving")

threads = []

for i in range(6):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

At most three threads can hold this semaphore at the same time.

### How It Works

- `acquire()` takes one available permit.
- If no permits are available, the thread waits.
- `release()` returns a permit.
- The initial permit count is the value supplied to `Semaphore()`; the default is `1`.

```python
semaphore = threading.Semaphore(3)
```

This allows up to three threads to enter the protected section simultaneously.

## 6. BoundedSemaphore

`BoundedSemaphore` behaves like `Semaphore`, but checks that releases do not increase the permit count above its initial value.

```python
import threading

semaphore = threading.BoundedSemaphore(2)

semaphore.acquire()
semaphore.release()
```

If too many releases occur and the count would exceed its initial value, Python raises `ValueError`.

A normal `Semaphore` allows extra releases, so its permit count can grow beyond the initial count.

## 7. Lock vs. Semaphore

| Lock | Semaphore |
|---|---|
| Provides mutual exclusion: one thread holds it at a time. | Allows a configured number of threads to hold permits simultaneously. |
| Useful for protecting shared data. | Useful for limiting access to a resource with limited capacity. |
| Has locked/unlocked states. | Maintains a permit counter. |

## 8. Important Safety Tips

- Protect shared mutable data when concurrent access could cause incorrect results.
- Prefer `with lock:` so locks are released reliably.
- Keep locked sections as short as practical.
- Acquire multiple locks in a consistent order to reduce deadlock risk.
- Choose `Lock`, `RLock`, or a semaphore according to the problem.


## Back to the main page
1. [← Back to Threading Notes](./015_multi_threading.md)

2. [Next: Inter-Thread Communication](./017_inter_thread_communication.md) — Events, Conditions, and Queues.