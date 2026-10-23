
# Python File Handling — Complete Notes

## 1. What Is File Handling?

File handling means creating, reading, writing, updating, and managing files using Python.

It allows a program to store data permanently so that the data can be used even after the program has stopped running.

### Real-life examples

- Saving student marks in a text file.
- Storing customer records in a CSV file.
- Reading configuration settings from a file.
- Compressing files into a ZIP archive.
- Saving and restoring Python objects.

---

## 2. Types of Files

Python commonly works with two broad categories of files.

### 2.1 Text Files

Text files store data as text, which is decoded into characters when opened in text mode.

Examples:

- `.txt`
- `.csv`
- `.json`
- `.py`
- `.md`

Example content in `student.txt`:

```text
Name: Shiv
Marks: 85
City: Pune
```

### 2.2 Binary Files

Binary files contain bytes rather than text decoded through a text encoding.

Examples:

- Images: `.jpg`, `.png`
- Audio: `.mp3`, `.wav`
- Video: `.mp4`
- ZIP archives: `.zip`
- Some document and executable formats

Binary files are normally opened using modes such as `rb` and `wb`.

**Important:** Text and binary refer to how data is handled by the program. A text file also has a byte representation when stored on disk.

---

## 3. Opening a File

Python provides the built-in `open()` function to open files.

### Syntax

```python
file = open(filename, mode)
```

Example:

```python
file = open("student.txt", "r")
```

Explanation:

- `student.txt` is the file name.
- `"r"` is the mode.
- `file` is a file object used to read or write data.

If a file does not exist and you open it in read mode, Python raises `FileNotFoundError`.

### Recommended Approach

Use the `with` statement whenever practical. It closes the file automatically.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

---

## 4. File Opening Modes

The mode determines what operations are allowed and what happens when the file is opened.

| Mode | Purpose | Creates missing file? | Truncates existing file? |
|---|---|---|---|
| `r` | Read | No | No |
| `r+` | Read and write | No | No |
| `w` | Write | Yes | Yes |
| `w+` | Read and write | Yes | Yes |
| `a` | Append | Yes | No |
| `a+` | Read and append | Yes | No |
| `x` | Exclusive creation for writing | Yes | No; fails if file exists |

### 4.1 Read Mode — `r`

Opens an existing file for reading.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

If the file does not exist, Python raises `FileNotFoundError`.

### 4.2 Read and Write Mode — `r+`

Opens an existing file for both reading and writing without initially deleting its contents.

```python
with open("student.txt", "r+", encoding="utf-8") as file:
    print(file.read())
    file.seek(0)
    file.write("Hello")
```

**Important:** `r+` does not truncate the file. Writing can overwrite existing characters, and if the new content is shorter, leftover characters may remain.

### 4.3 Write Mode — `w`

Creates a file if it does not exist. If it already exists, its contents are truncated when opened.

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")
```

**Warning:** Existing content is erased. Use this mode carefully.

### 4.4 Read and Write Mode — `w+`

Creates a file if necessary and truncates an existing file.

```python
with open("student.txt", "w+", encoding="utf-8") as file:
    file.write("Python File Handling")
    file.seek(0)
    print(file.read())
```

Output:

```text
Python File Handling
```

The `seek(0)` call moves the file position to the beginning before reading.

### 4.5 Append Mode — `a`

Adds new data at the end of a file without truncating the existing content.

```python
with open("student.txt", "a", encoding="utf-8") as file:
    file.write("\nCity: Pune")
```

If the file does not exist, Python creates it.

### 4.6 Append and Read Mode — `a+`

Allows reading and appending.

```python
with open("student.txt", "a+", encoding="utf-8") as file:
    file.write("\nNew information")
    file.seek(0)
    print(file.read())
```

The `seek(0)` call is needed here to read from the beginning.

In append mode, writes go to the end of the file even if you move the file position elsewhere.

### 4.7 Exclusive Creation Mode — `x`

Creates a new file only if it does not already exist.

```python
with open("new_file.txt", "x", encoding="utf-8") as file:
    file.write("This is a new file.")
```

If `new_file.txt` already exists, Python raises `FileExistsError`.

This mode is useful when you do not want to overwrite an existing file.

---

## 5. Binary File Modes

Add `b` to a suitable mode to open a file in binary mode.

Common examples:

- `rb`: Read binary data.
- `wb`: Write binary data.
- `ab`: Append binary data.
- `rb+` or `r+b`: Read and write binary data.
- `wb+` or `w+b`: Read and write, truncating existing content.
- `ab+` or `a+b`: Read and append binary data.
- `xb` or `xb+`: Exclusively create a binary file.

Both orders shown for combined modes, such as `rb+` and `r+b`, are accepted.

### Example: Read a Binary File

```python
with open("photo.jpg", "rb") as file:
    data = file.read()

print(type(data))
print(len(data))
```

The result of `read()` in binary mode is a `bytes` object.

### Example: Copy a Binary File

```python
with open("photo.jpg", "rb") as source:
    with open("photo_copy.jpg", "wb") as destination:
        while True:
            chunk = source.read(8192)

            if not chunk:
                break

            destination.write(chunk)
```

This copies a file in chunks instead of loading the entire file into memory.

---

## 6. Closing a File

The `close()` method closes an open file.

```python
file = open("student.txt", "r", encoding="utf-8")

print(file.read())

file.close()
```

Closing files is important because it releases resources and ensures pending writes are handled appropriately.

### Check Whether a File Is Closed

```python
file = open("student.txt", "r", encoding="utf-8")

print(file.closed)

file.close()

print(file.closed)
```

Output:

```text
False
True
```

**Best practice:** Prefer `with open(...)` because it closes the file automatically, even if an exception occurs inside the block.

---

## 7. Writing Text Data

Python provides `write()` and `writelines()` for writing text.

### 7.1 `write()`

Writes a string to the file and returns the number of characters written.

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("File Handling")
```

The `\n` character creates a new line.

`write()` does not automatically add a newline.

### 7.2 `writelines()`

Writes an iterable of strings to a file.

```python
lines = [
    "Name: Shiv\n",
    "Marks: 85\n",
    "City: Pune\n"
]

with open("student.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

**Important:** `writelines()` does not automatically insert newline characters. Include `\n` in the strings when you need separate lines.

---

## 8. Reading Text Data

Python provides several ways to read text from a file.

Assume `student.txt` contains:

```text
Name: Shiv
Marks: 85
City: Pune
```

### 8.1 `read()`

Reads all remaining content when called without a size, or reads up to the requested number of characters.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

To read the first five characters:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.read(5))
```

Output:

```text
Name:
```

### 8.2 `readline()`

Reads one line at a time.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())
```

Each returned line usually includes its newline character if one exists.

### 8.3 `readlines()`

Reads the remaining lines and returns them as a list of strings.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

Example output:

```text
['Name: Shiv\n', 'Marks: 85\n', 'City: Pune\n']
```

The exact output depends on the file's contents and newline characters.

### 8.4 Recommended: Iterate Over the File

For large files, iterating over lines is often more memory-efficient than loading all content at once.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))
```

---

## 9. The `with` Statement

The `with` statement uses a context manager to manage a resource.

For file handling, it automatically closes the file when the block finishes, including when an exception occurs.

### Example

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

print("File operation completed")
```

There is no need to call `file.close()` explicitly.

### Why Is It Better?

- Helps prevent forgotten file closures.
- Handles cleanup even when an exception occurs.
- Makes code cleaner and safer.

---

## 10. `tell()` and `seek()`

These methods help you work with the current position in a file.

### 10.1 `tell()`

Returns the current stream position.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.tell())
    file.read(5)
    print(file.tell())
```

For simple ASCII text in the usual environment, the output will commonly be:

```text
0
5
```

The exact position depends on the encoding and stream. In text mode, the returned position is an opaque position marker, not always a simple character index.

### 10.2 `seek()`

Moves the file position to a specified location or position marker.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.read(5))
    file.seek(0)
    print(file.read(5))
```

Output:

```text
Name:
Name:
```

Here, `seek(0)` returns to the beginning of the file.

### Binary File Example

In binary mode, offsets are measured in bytes.

```python
with open("data.bin", "rb") as file:
    file.seek(5)
    print(file.tell())
    print(file.read(3))
```

The example assumes `data.bin` contains at least eight bytes.

---

## 11. Handling CSV Files

CSV means Comma-Separated Values. It is a common format for storing tabular data.

Example `students.csv`:

```csv
name,marks,city
Shiv,85,Pune
Amit,90,Mumbai
Priya,92,Nashik
```

Python provides the built-in `csv` module.

### 11.1 Read a CSV File

```python
import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Example output:

```text
['name', 'marks', 'city']
['Shiv', '85', 'Pune']
['Amit', '90', 'Mumbai']
['Priya', '92', 'Nashik']
```

### 11.2 Write a CSV File

```python
import csv

students = [
    ["name", "marks", "city"],
    ["Shiv", 85, "Pune"],
    ["Amit", 90, "Mumbai"],
    ["Priya", 92, "Nashik"]
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)
```

This creates or overwrites `students.csv`.

### 11.3 Read CSV Rows as Dictionaries

```python
import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(student["name"], student["marks"])
```

Output:

```text
Shiv 85
Amit 90
Priya 92
```

### 11.4 Write CSV Dictionaries

```python
import csv

students = [
    {"name": "Shiv", "marks": 85, "city": "Pune"},
    {"name": "Amit", "marks": 90, "city": "Mumbai"}
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "marks", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)
```

**Best practice:** Use the `csv` module instead of manually splitting lines by commas, because CSV values may contain commas, quotes, or newline characters.

---

## 12. Zipping and Unzipping Files

Python's built-in `zipfile` module can create and extract ZIP archives.

### 12.1 Create a ZIP File

```python
from zipfile import ZipFile, ZIP_DEFLATED

with ZipFile("backup.zip", "w", compression=ZIP_DEFLATED) as archive:
    archive.write("student.txt")
```

This adds `student.txt` to `backup.zip`.

The source file must exist.

### 12.2 Add Multiple Files

```python
from zipfile import ZipFile, ZIP_DEFLATED

files = ["student.txt", "students.csv"]

with ZipFile("backup.zip", "w", compression=ZIP_DEFLATED) as archive:
    for filename in files:
        archive.write(filename)
```

Each listed file must exist in the current working directory or at its specified path.

### 12.3 List Files Inside a ZIP Archive

```python
from zipfile import ZipFile

with ZipFile("backup.zip", "r") as archive:
    print(archive.namelist())
```

### 12.4 Extract a ZIP File

```python
from zipfile import ZipFile

with ZipFile("backup.zip", "r") as archive:
    archive.extractall("extracted_files")
```

This extracts the archive into the `extracted_files` directory.

**Security warning:** Only extract trusted archives, and be careful with archives containing unexpected paths or files. Do not blindly extract untrusted ZIP files.

---

## 13. Get Information About a File

Python provides the `os` module and `os.stat()` to retrieve file metadata.

```python
import os

stats = os.stat("student.txt")

print("Size:", stats.st_size, "bytes")
print("Last access time:", stats.st_atime)
print("Last modification time:", stats.st_mtime)
print("Metadata change time:", stats.st_ctime)
```

### Common `os.stat()` Attributes

| Attribute | Meaning |
|---|---|
| `st_mode` | File type and permission bits |
| `st_ino` | Inode number, where supported |
| `st_dev` | Device identifier |
| `st_nlink` | Number of hard links |
| `st_uid` | Owner user ID, where supported |
| `st_gid` | Owner group ID, where supported |
| `st_size` | File size in bytes |
| `st_atime` | Most recent access time |
| `st_mtime` | Most recent content modification time |
| `st_ctime` | Platform-dependent: often metadata change time on Unix-like systems; creation time on Windows |

**Important:** The availability and meaning of some attributes vary by operating system.

### Convert Timestamps to Readable Dates

```python
import os
from datetime import datetime

stats = os.stat("student.txt")

modified_time = datetime.fromtimestamp(stats.st_mtime)

print("Last modified:", modified_time)
```

### Check Whether a File Exists

```python
import os

if os.path.exists("student.txt"):
    print("File exists")
else:
    print("File does not exist")
```

For more modern path operations, Python also provides `pathlib`.

---

## 14. Pickling and Unpickling

Pickling converts a Python object into a byte stream so it can be saved. Unpickling reconstructs an object from that byte stream.

Python provides the built-in `pickle` module.

### 14.1 Pickling with `dump()`

```python
import pickle

student = {
    "name": "Shiv",
    "marks": 85,
    "city": "Pune"
}

with open("student.dat", "wb") as file:
    pickle.dump(student, file)
```

Here:

- `pickle.dump()` serializes the object.
- `"wb"` opens the file for binary writing.
- The object is stored in `student.dat`.

### 14.2 Unpickling with `load()`

```python
import pickle

with open("student.dat", "rb") as file:
    student = pickle.load(file)

print(student)
```

Output:

```text
{'name': 'Shiv', 'marks': 85, 'city': 'Pune'}
```

### 14.3 Pickle Multiple Objects

You can write multiple objects sequentially and load them in the same order.

```python
import pickle

with open("data.pkl", "wb") as file:
    pickle.dump([1, 2, 3], file)
    pickle.dump({"name": "Shiv"}, file)

with open("data.pkl", "rb") as file:
    first = pickle.load(file)
    second = pickle.load(file)

print(first)
print(second)
```

Output:

```text
[1, 2, 3]
{'name': 'Shiv'}
```

### Security Warning

**Never unpickle data from an untrusted source.** Loading a malicious pickle file can execute arbitrary code.

Pickle is Python-specific and is not a general-purpose, language-independent data exchange format. For simple data exchange, consider JSON or CSV where appropriate.

---

## 15. Handling File Exceptions

File operations may fail for different reasons.

Common exceptions include:

- `FileNotFoundError`: The file does not exist.
- `PermissionError`: The program lacks the required permission.
- `IsADirectoryError`: A directory was used where a file was expected.
- `UnicodeDecodeError`: The file's bytes cannot be decoded using the chosen text encoding.
- `OSError`: A broader category of operating-system-related errors.

### Example

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("The file was not found.")

except PermissionError:
    print("You do not have permission to read this file.")
```

Use specific exception handling when you know how to respond to a particular error.

---

## 16. Text Mode vs Binary Mode

| Feature | Text Mode | Binary Mode |
|---|---|---|
| Common modes | `r`, `w`, `a` | `rb`, `wb`, `ab` |
| Data handled as | `str` | `bytes` |
| Encoding | Text encoding is used | No text decoding is performed |
| Newline handling | May translate newlines | Reads and writes bytes directly |
| Common use | Text, CSV, JSON, source code | Images, audio, video, ZIP files |

---

## 17. Important Best Practices

1. Prefer `with open(...)` over manually opening and closing files.
2. Specify `encoding="utf-8"` when working with text files unless another encoding is required.
3. Use `newline=""` when opening CSV files with the `csv` module.
4. Use binary mode for raw bytes, images, and other binary formats.
5. Be careful with `"w"` and `"w+"` because they truncate existing files.
6. Use chunked reads for large binary files.
7. Handle file errors appropriately.
8. Never unpickle untrusted data.
9. Validate ZIP archives before extracting untrusted files.
10. Prefer `pathlib` for readable, cross-platform path handling.

---

## 18. Practice Questions

1. What is file handling?
2. What is the difference between text and binary files?
3. What happens when an existing file is opened using `"w"`?
4. What is the difference between `"w"` and `"a"`?
5. What is the purpose of `"x"` mode?
6. What is the difference between `write()` and `writelines()`?
7. What is the difference between `readline()` and `readlines()`?
8. Why is the `with` statement recommended?
9. What do `seek()` and `tell()` do?
10. Why should we use Python's `csv` module?
11. Which module can create ZIP archives?
12. What does `os.stat()` return?
13. What is pickling?
14. Why should you never unpickle untrusted data?
15. What is the difference between `str` and `bytes`?

### Short Answers

1. Reading, writing, creating, and managing files.
2. Text mode decodes bytes into text; binary mode handles bytes directly.
3. Its existing contents are truncated.
4. `"w"` overwrites existing content; `"a"` adds content at the end.
5. To create a new file only if it does not already exist.
6. `write()` writes a string; `writelines()` writes an iterable of strings without adding newlines automatically.
7. `readline()` reads one line; `readlines()` returns remaining lines in a list.
8. It automatically closes the file after the block finishes.
9. `tell()` reports the current position marker; `seek()` changes the position.
10. It correctly handles CSV quoting and delimiters.
11. `zipfile`.
12. File metadata in an `os.stat_result` object.
13. Serializing a Python object into a byte stream.
14. Malicious pickle data can execute arbitrary code.
15. `str` represents text; `bytes` represents a sequence of byte values.
