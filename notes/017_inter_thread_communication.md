
# Inter-Thread Communication in Python

## 1. What Is Inter-Thread Communication?

Inter-thread communication means allowing threads to coordinate with one another or share information.

For example, imagine a producer thread that creates items and a consumer thread that processes those items. The consumer needs to know when an item is available.

Python supports several communication mechanisms, including:

1. `Event`
2. `Condition`
3. `Queue`

## 2. Event Objects

An `Event` allows one thread to signal another thread.

An event maintains an internal flag:

- `set()` changes the flag to `True`.
- `clear()` changes the flag to `False`.
- `wait()` waits until the flag becomes `True`.
- `is_set()` checks whether the flag is set.

### Example

```python
import threading
import time

event = threading.Event()

def consumer():
    print("Consumer is waiting...")
    event.wait()
    print("Signal received. Consumer can continue.")

t = threading.Thread(target=consumer)
t.start()

time.sleep(2)

print("Producer sends signal")
event.set()

t.join()
```

The consumer waits until the producer sets the event.

**Important:** Once the event is set, waiting threads can continue. The event remains set until `clear()` is called.

Use `is_set()` instead of the older `isSet()` method.

## 3. Condition Objects

A `Condition` allows threads to wait until a particular state or condition is satisfied.

A condition is associated with a lock, which it uses to coordinate access to shared state.

Important methods:

- `acquire()` — acquires the associated lock.
- `release()` — releases the associated lock.
- `wait()` — releases the lock and waits for notification; it reacquires the lock before returning.
- `notify()` — wakes one waiting thread.
- `notify_all()` — wakes all waiting threads.

### Example: Wait for Data

```python
import threading

condition = threading.Condition()
data_ready = False

def consumer():
    global data_ready

    with condition:
        while not data_ready:
            condition.wait()

        print("Consumer: data is ready")

def producer():
    global data_ready

    with condition:
        data_ready = True
        print("Producer: data is ready")
        condition.notify()

t = threading.Thread(target=consumer)
t.start()

producer()

t.join()
```

The consumer checks the condition while holding the lock. When it calls `wait()`, it releases the lock and waits for notification.

**Why use `while` instead of `if`?**

A notification does not guarantee that the condition is still true when the waiting thread resumes. The thread should check the condition again.

## 4. Queue Objects

A `Queue` is a convenient way for threads to exchange data safely.

Python's `queue` module provides thread-safe queues. These queues handle the necessary synchronization internally.

```python
import queue

q = queue.Queue()
```

### Important Methods

| Method | Purpose |
|---|---|
| `put(item)` | Adds an item to the queue. |
| `get()` | Removes and returns the next item. |
| `task_done()` | Indicates that a retrieved item has been processed. |
| `join()` | Waits until all queued tasks have been marked complete. |

By default, `put()` waits if a bounded queue is full, and `get()` waits if the queue is empty. Optional timeout and non-blocking arguments can change this behaviour.

### Example: Producer and Consumer

```python
import queue
import threading

q = queue.Queue()

def producer():
    for item in ["Apple", "Banana", "Mango"]:
        q.put(item)
        print("Produced:", item)

    q.put(None)  # Sentinel indicates there are no more items

def consumer():
    while True:
        item = q.get()

        try:
            if item is None:
                break

            print("Consumed:", item)
        finally:
            q.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

consumer_thread.start()
producer_thread.start()

producer_thread.join()
q.join()
consumer_thread.join()
```

The producer places items in the queue. The consumer retrieves and processes them.

The `None` value is a sentinel that tells the consumer to stop. The example assumes `None` is not a normal data item.

## 5. Types of Queues

Python provides several queue types.

### 5.1 FIFO Queue

FIFO means **First In, First Out**.

The first item inserted is the first item removed.

```python
import queue

q = queue.Queue()

q.put("A")
q.put("B")
q.put("C")

print(q.get())  # A
print(q.get())  # B
print(q.get())  # C
```

### 5.2 LIFO Queue

LIFO means **Last In, First Out**.

The most recently inserted item is removed first.

```python
import queue

q = queue.LifoQueue()

q.put("A")
q.put("B")
q.put("C")

print(q.get())  # C
print(q.get())  # B
print(q.get())  # A
```

### 5.3 Priority Queue

A priority queue retrieves items according to priority rather than simple insertion order.

```python
import queue

q = queue.PriorityQueue()

q.put((2, "Normal"))
q.put((1, "Urgent"))
q.put((3, "Low"))

print(q.get())  # (1, 'Urgent')
print(q.get())  # (2, 'Normal')
print(q.get())  # (3, 'Low')
```

For tuples, the queue orders items by their first comparable element, then uses later elements to break ties.

## 6. Event vs. Condition vs. Queue

| Mechanism | Best suited for |
|---|---|
| `Event` | Signalling that something has happened. |
| `Condition` | Waiting for and notifying about changes to shared state. |
| `Queue` | Safely transferring work items or data between threads. |

## 7. Quick Revision

- `Event` uses a flag to signal threads.
- `Condition` supports waiting for a state change and notifying waiting threads.
- `Queue` provides a thread-safe way to share items.
- FIFO removes the oldest item first.
- LIFO removes the newest item first.
- `PriorityQueue` removes items according to priority.
- Use `task_done()` and `join()` when you need to track completion of queued work.

## Back to the main page
1. [← Back to Threading Notes](./015_multi_threading.md)
2. [Nex: Threading Quick Revision](./018_threading_quick_revision.md) — Important methods, comparisons, and practice questions.