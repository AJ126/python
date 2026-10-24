
# Python Threading

## 1. What Is Multitasking?

**Multitasking** means handling multiple tasks during the same period.

There are two common types of multitasking:

### 1.1 Process-Based Multitasking

Executing multiple independent processes during the same period is called process-based multitasking.

**Example:** Listening to music while writing Python code and downloading a file. These activities may be handled by different processes.

### 1.2 Thread-Based Multitasking

Executing multiple threads within a program is called thread-based multitasking.

A **thread** is a sequence of instructions that can execute independently within a process.

**Example:** A web application can use one thread to handle one task while another thread handles a different task.

### Benefits of Multitasking

- Can improve responsiveness.
- Can help overlap waiting operations.
- Can make applications more responsive when handling independent tasks.

> Multitasking does not guarantee that every program will run faster. The benefit depends on the workload and the system.

## 2. Applications of Multithreading

Multithreading can be useful in:

1. Multimedia applications.
2. Animations and games.
3. Web and application servers.
4. Applications that perform multiple waiting operations.
5. Background tasks, such as downloading data.

## 3. Python `threading` Module

Python provides the built-in `threading` module to create and manage threads.

```python
import threading
```

Every Python program starts with a main thread.

## 4. Creating a Thread

There are three common approaches to creating threads.

1. Pass a function to `threading.Thread()`.
2. Create a class that extends `threading.Thread`.
3. Create a class that does not extend `threading.Thread`, then pass its method to a thread.

### 4.1 Creating a Thread Without Creating a Class

```python
import threading

def show_numbers():
    for i in range(5):
        print("Child thread:", i)

t = threading.Thread(target=show_numbers)

t.start()
t.join()

print("Main thread finished")
```

**Explanation:**

- `threading.Thread()` creates a thread object.
- `target=show_numbers` specifies the function the thread should execute.
- `start()` starts the thread.
- `join()` makes the main thread wait until this thread finishes.

Call `show_numbers`, not `show_numbers()`, when passing it as the target.

### 4.2 Creating a Thread by Extending `Thread`

Create a child class of `threading.Thread` and override its `run()` method.

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("Child thread:", i)

t = MyThread()
t.start()
t.join()

print("Main thread finished")
```

When `start()` is called, Python arranges for `run()` to execute in the new thread.

**Important:** Calling `t.run()` directly does not start a new thread; it runs the method in the current thread.

### 4.3 Creating a Thread Without Extending `Thread`

You can define a normal class and pass one of its methods to `Thread`.

```python
import threading

class Worker:
    def show(self):
        for i in range(5):
            print("Working:", i)

worker = Worker()

t = threading.Thread(target=worker.show)
t.start()
t.join()
```

This approach is useful when the class already represents a worker or service.

## 5. Thread Execution Order

When multiple threads run, their execution order is not guaranteed.

```python
import threading

def show_numbers(name):
    for i in range(5):
        print(name, i)

t1 = threading.Thread(target=show_numbers, args=("Thread A",))
t2 = threading.Thread(target=show_numbers, args=("Thread B",))

t1.start()
t2.start()

t1.join()
t2.join()
```

The output order may differ between runs.

Use synchronization when your program requires a specific ordering or safe access to shared data.

## 6. Getting and Setting a Thread Name

Every thread has a name. Python assigns a default name, or you can provide one.

```python
import threading

def task():
    print("Current thread:", threading.current_thread().name)

t = threading.Thread(target=task, name="DownloadThread")

print("Thread name:", t.name)

t.start()
t.join()
```

Use the `.name` property to get or set a thread's name.

```python
t.name = "WorkerThread"
```

Older methods such as `getName()` and `setName()` are deprecated; prefer `.name`.

## 7. Useful Threading Functions and Methods

### `threading.active_count()`

Returns the number of currently active thread objects.

```python
import threading

print(threading.active_count())
```

### `threading.enumerate()`

Returns a list of currently active thread objects.

```python
import threading

for t in threading.enumerate():
    print(t.name)
```

### `is_alive()`

Checks whether a thread has been started and has not finished.

```python
import threading
import time

def task():
    time.sleep(2)

t = threading.Thread(target=task)
t.start()

print(t.is_alive())

t.join()
print(t.is_alive())
```

The first result will normally be `True`, and the second will be `False`.

### `join()`

Makes the calling thread wait until another thread finishes, or until an optional timeout expires.

```python
t.join()
```

## 8. Daemon Threads

A **daemon thread** is a background thread that does not keep the Python program alive by itself.

Daemon threads are useful for some background activities that may stop when the program exits. They should not be used for essential work that must finish reliably.

```python
import threading
import time

def background_task():
    while True:
        print("Background task running")
        time.sleep(1)

t = threading.Thread(target=background_task, daemon=True)
t.start()

print("Main program finished")
```

The program can exit even while the daemon thread is running. Its work may be interrupted.

### Checking Daemon Status

```python
print(t.daemon)
```

### Setting Daemon Status

```python
t.daemon = True
t.start()
```

Set the daemon status before calling `start()`. It cannot be changed after the thread has started.

### Default Daemon Status

- The main thread is non-daemon.
- A new thread normally inherits the daemon status of the thread that creates it.

> Note: Python's garbage collector is not a reliable example of a daemon thread. Do not assume garbage collection is performed by a daemon thread.

## 9. Quick Revision

- Multitasking means handling multiple tasks during the same period.
- Process-based multitasking involves independent processes.
- Thread-based multitasking involves multiple threads within a process.
- `threading.Thread()` creates a thread object.
- `start()` starts a new thread.
- `run()` contains the work performed by a thread.
- `join()` waits for a thread to finish.
- `.name` gets or sets a thread's name.
- `is_alive()` checks whether a thread is still active.
- `threading.active_count()` counts active threads.
- `threading.enumerate()` lists active threads.
- Daemon threads do not keep the Python program alive by themselves.



---

## Related Threading Notes

Continue learning about Python threading:

1. [Thread Synchronization](./016_thread_synchronization.md) — Locks, RLocks, Semaphores, and Bounded Semaphores.
2. [Inter-Thread Communication](./017_inter_thread_communication.md) — Events, Conditions, and Queues.
3. [Threading Quick Revision](./018_threading_quick_revision.md) — Important methods, comparisons, and practice questions.
