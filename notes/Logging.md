
# Python Logging

## 1. What Is Logging?

**Logging** is the process of recording information about an application's execution, including important events, warnings, errors, and exceptions.

It is highly recommended to store useful application-flow information and exception details in a log file so that developers can understand what happened during execution.

### Advantages of Logging

1. **Debugging:** Log files help developers identify and fix errors.
2. **Monitoring:** We can track application behavior and identify problems.
3. **Statistics:** We can record information such as the number of requests received per day.
4. **Error tracking:** We can store exception details for later investigation.
5. **Maintenance:** Logs help us understand what happened before a failure.

Python provides an in-built module called `logging` to implement logging.

```python
import logging
```

---

## 2. Logging Levels in Python

Python provides six standard logging levels. Each level represents the importance or severity of a message.

| Logging Level | Numeric Value | Purpose |
|---|---:|---|
| `CRITICAL` | 50 | A very serious problem requiring immediate attention |
| `ERROR` | 40 | A serious error that prevents an operation from completing successfully |
| `WARNING` | 30 | An indication of a possible problem or unexpected situation |
| `INFO` | 20 | General information about application execution |
| `DEBUG` | 10 | Detailed information useful for debugging |
| `NOTSET` | 0 | Indicates that no specific logging threshold has been set at that logger |

### Example

```python
import logging

logging.critical("Critical problem occurred")
logging.error("An error occurred")
logging.warning("This is a warning")
logging.info("Application started")
logging.debug("Debugging information")
```

By default, Python's root logger normally displays messages at `WARNING` level and above.

Therefore, the output will be similar to:

```text
CRITICAL:root:Critical problem occurred
ERROR:root:An error occurred
WARNING:root:This is a warning
```

The `INFO` and `DEBUG` messages are not displayed because their levels are below the default threshold.

**Important:** `NOTSET` is a configuration level, not a message severity that is normally used like `INFO` or `ERROR`.

---

## 3. How to Implement Logging

Python provides the `basicConfig()` function in the `logging` module to configure basic logging.

We can specify:

- The log file name
- The minimum logging level
- The message format
- The date and time format

### Syntax

```python
logging.basicConfig(
    filename="log.txt",
    level=logging.WARNING
)
```

### Explanation

- `filename="log.txt"`: Writes log messages to a file named `log.txt`.
- `level=logging.WARNING`: Records `WARNING`, `ERROR`, and `CRITICAL` messages.
- Messages below the configured threshold, such as `INFO` and `DEBUG`, are ignored.

### Example: Store Logs in a File

```python
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.WARNING
)

logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Disk space is getting low")
logging.error("Unable to process the request")
logging.critical("Application cannot continue")
```

After running the program, `log.txt` will contain messages similar to:

```text
WARNING:root:Disk space is getting low
ERROR:root:Unable to process the request
CRITICAL:root:Application cannot continue
```

The file is created if necessary, provided the application has permission to write to the target directory.

**Note:** `basicConfig()` normally has no effect if the root logger has already been configured with handlers. In a fresh script, configure logging before making logging calls.

---

## 4. Logging Levels: Practical Example

Suppose we want to record all levels of messages in a file.

```python
import logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debugging details")
logging.info("Application started")
logging.warning("Unexpected input received")
logging.error("Unable to save the record")
logging.critical("A critical failure occurred")
```

### Explanation

- `level=logging.DEBUG`: Allows all five standard message severities, from `DEBUG` through `CRITICAL`, to be recorded.
- `%(asctime)s`: Includes the timestamp.
- `%(levelname)s`: Includes the logging level.
- `%(message)s`: Includes the actual message.

### Sample Log Output

```text
2026-10-23 10:30:00,123 - DEBUG - Debugging details
2026-10-23 10:30:00,124 - INFO - Application started
2026-10-23 10:30:00,125 - WARNING - Unexpected input received
2026-10-23 10:30:00,126 - ERROR - Unable to save the record
2026-10-23 10:30:00,127 - CRITICAL - A critical failure occurred
```

The timestamps above are illustrative examples.

---

## 5. Logging Exceptions

Logging is particularly useful when an exception occurs because we can save the error information for later debugging.

### Example Using `logging.error()`

```python
import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR
)

try:
    result = 10 / 0

except ZeroDivisionError as error:
    logging.error("An exception occurred: %s", error)
```

The log file will contain a message similar to:

```text
ERROR:root:An exception occurred: division by zero
```

### Logging the Complete Exception Traceback

Use `logging.exception()` inside an exception handler when you want to record the exception message and traceback.

```python
import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception("An exception occurred while calculating the result")
```

The log contains the message and traceback information that helps identify where the exception occurred.

**Important:** `logging.exception()` should normally be called from inside an `except` block.

---

## 6. Logging Levels and Their Thresholds

The configured logging level acts as a minimum threshold.

For example:

```python
logging.basicConfig(level=logging.WARNING)
```

This allows `WARNING`, `ERROR`, and `CRITICAL` messages.

| Configured Level | Messages Normally Recorded |
|---|---|
| `DEBUG` | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| `INFO` | INFO, WARNING, ERROR, CRITICAL |
| `WARNING` | WARNING, ERROR, CRITICAL |
| `ERROR` | ERROR, CRITICAL |
| `CRITICAL` | CRITICAL |

A message must meet or exceed the configured threshold to pass that logger's level filter.

---

## 7. Important Logging Functions

| Function | Purpose |
|---|---|
| `logging.debug()` | Records debugging details |
| `logging.info()` | Records general application information |
| `logging.warning()` | Records warnings |
| `logging.error()` | Records errors |
| `logging.critical()` | Records critical problems |
| `logging.exception()` | Records an error message with exception traceback information |
| `logging.basicConfig()` | Configures basic logging |
| `logging.shutdown()` | Flushes and closes logging handlers during shutdown |

---

## 8. Best Practices

1. Choose an appropriate logging level for each message.
2. Include useful context in log messages.
3. Use `logging.exception()` inside an exception handler when a traceback is needed.
4. Configure logging near the start of the application.
5. Avoid logging passwords, access tokens, or other sensitive information.
6. For larger applications, use named loggers with `logging.getLogger(__name__)`.
7. Consider log rotation for long-running applications so log files do not grow indefinitely.
8. Use a proper logging configuration in production applications.

---

## 9. Practice Questions

1. What is logging in Python?
2. What are the advantages of logging?
3. Which built-in module is used for logging?
4. What are the six standard logging levels?
5. What is the purpose of `logging.basicConfig()`?
6. What is the difference between `logging.error()` and `logging.exception()`?
7. Why might `INFO` messages not appear when using the default configuration?
8. How can we store log messages in a file?
9. What does `%(asctime)s` represent in a logging format?
10. Why should we avoid logging passwords and access tokens?

### Practice Program

Write a Python program that:

1. Accepts two numbers from the user.
2. Divides the first number by the second.
3. Handles invalid input and division by zero.
4. Records successful calculations using `logging.info()`.
5. Records exceptions using `logging.exception()`.
6. Stores the logs in a file named `calculator.log`.
