 
# Python Threading — Quick Revision

## 1. Important Thread Methods

| Method or function | Purpose |
|---|---|
| `Thread(target=func)` | Creates a thread configured to run a function. |
| `start()` | Starts a new thread. |
| `run()` | Contains the thread's work; calling it directly does not start a new thread. |
| `join()` | Waits for a thread to finish. |
| `.name` | Gets or sets the thread's name. |
| `is_alive()` | Checks whether a thread is still active. |
| `.daemon` | Gets or sets daemon status before the thread starts. |
| `threading.current_thread()` | Returns the current thread object. |
| `threading.active_count()` | Counts active thread objects. |
| `threading.enumerate()` | Returns a list of active thread objects. |

## 2. Thread Creation Approaches

### Function as the target

```python
import threading

def task():
    print("Task running")

t = threading.Thread(target=task)
t.start()
t.join()
```

### Extend `Thread`

```python
import threading

class Worker(threading.Thread):
    def run(self):
        print("Task running")

t = Worker()
t.start()
t.join()
```

### Use a method from another class

```python
import threading

class Worker:
    def task(self):
        print("Task running")

worker = Worker()
t = threading.Thread(target=worker.task)
t.start()
t.join()
```

## 3. Synchronization Comparison

| Tool | Main purpose |
|---|---|
| `Lock` | Allows one thread to hold the lock at a time. |
| `RLock` | Allows the owning thread to acquire the same lock repeatedly. |
| `Semaphore(n)` | Limits simultaneous access to `n` permits. |
| `BoundedSemaphore(n)` | Like a semaphore, but detects releases that exceed the initial permit count. |

## 4. Communication Comparison

| Tool | Main purpose |
|---|---|
| `Event` | Signal threads using a shared flag. |
| `Condition` | Wait for a state change and notify waiting threads. |
| `Queue` | Transfer data safely between threads. |

## 5. Queue Types

| Queue | Behaviour |
|---|---|
| `queue.Queue()` | FIFO — First In, First Out. |
| `queue.LifoQueue()` | LIFO — Last In, First Out. |
| `queue.PriorityQueue()` | Retrieves items according to priority. |

## 6. Common Mistakes

1. Writing `target=task()` instead of `target=task`.
2. Calling `run()` when the intention is to start a new thread.
3. Assuming threads will always execute in the same order.
4. Forgetting to release a manually acquired lock.
5. Changing `.daemon` after the thread has started.
6. Accessing shared mutable data without suitable synchronization.
7. Calling `Queue.join()` without ensuring that each retrieved item gets a matching `task_done()` call.
8. Assuming a daemon thread will finish its work before the program exits.

## Back to the main page
[← Back to Threading Notes](./015_multi_threading.md)
