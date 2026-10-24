# Python Important Notes: Database Programming

## 04. Database Programming Using Python

### Q1. What is database programming using Python?

**Answer:**

Database programming using Python means using a Python program to perform CRUD operations on a database.

CRUD stands for:

| Operation | Full form | Meaning |
|---|---|---|
| C | Create | Insert or store data |
| R | Read | Retrieve data |
| U | Update | Modify existing data |
| D | Delete | Remove data |

**Example:** An employee management application can use Python to insert employee details, display employees, update salaries, and delete employee records.

### Q2. What are the steps involved in Python database programming?

**Answer:**

1. Establish a connection with the database server.
2. Create a cursor object.
3. Submit SQL statements using the cursor.
4. Commit the transaction after `INSERT`, `UPDATE`, or `DELETE` operations.
5. Close the cursor object.
6. Close the database connection.

### Q3. What is the role of a cursor object in Python database programming?

**Answer:**

A cursor object has two main roles:

1. It submits SQL statements to the database management system (DBMS).
2. It retrieves and provides access to query results.

For example:

```python
cursor.execute("SELECT * FROM EMPLOYEE")
records = cursor.fetchall()
```

Here, `execute()` runs the SQL query, and `fetchall()` retrieves all returned records.

---

## 05. Connecting Python to MySQL

Before running the examples, install the MySQL connector package:

```bash
python -m pip install mysql-connector-python
```

The examples below assume:

- MySQL Server is running on your computer.
- A database named `empdb` exists.
- A table named `EMPLOYEE` exists with columns `EMPNO`, `NAME`, and `SALARY`.
- Your MySQL username and password are configured correctly.

Example table structure:

```sql
CREATE DATABASE empdb;

USE empdb;

CREATE TABLE EMPLOYEE (
    EMPNO INT PRIMARY KEY,
    NAME VARCHAR(100),
    SALARY DECIMAL(10, 2)
);
```

The database and table need to be created only once.

### Common connection example

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="empdb"
)

cursor = connection.cursor()
```

Replace `your_password` with your actual MySQL password. Do not share real passwords in public code repositories.

---

## 06. Insert an Employee Record

### Q4. Write a Python program that stores employee data in the database.

**File:** `storeemployee.py`

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="empdb"
)

cursor = connection.cursor()

sql = """
    INSERT INTO EMPLOYEE (EMPNO, NAME, SALARY)
    VALUES (%s, %s, %s)
"""

values = (1002, "Rahim", 50000)

cursor.execute(sql, values)
connection.commit()

print("Number of employees inserted:", cursor.rowcount)

cursor.close()
connection.close()
```

**Explanation:**

- `connect()` establishes the database connection.
- `cursor()` creates a cursor object.
- `execute()` runs the SQL `INSERT` statement.
- `commit()` saves the transaction.
- `rowcount` reports the number of affected rows.

**Important:** The employee number must not already exist because `EMPNO` is the primary key.

---

## 07. Update Employee Records

### Q5. Write a Python program that updates employee salaries.

**File:** `updateemployee.py`

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="empdb"
)

cursor = connection.cursor()

sql = "UPDATE EMPLOYEE SET SALARY = SALARY + 1000"

cursor.execute(sql)
connection.commit()

print("Number of employees updated:", cursor.rowcount)

cursor.close()
connection.close()
```

**Explanation:**

- `UPDATE EMPLOYEE` modifies employee records.
- `SALARY = SALARY + 1000` increases each employee's salary by 1000.
- Since there is no `WHERE` clause, the update applies to all employees.

To update only one employee, use a condition:

```python
sql = "UPDATE EMPLOYEE SET SALARY = SALARY + %s WHERE EMPNO = %s"
cursor.execute(sql, (1000, 1001))
```

This increases the salary of employee `1001` by 1000.

---

## 08. Delete Employee Records

### Q6. Write a Python program that deletes an employee record.

**File:** `deleteemployee.py`

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="empdb"
)

cursor = connection.cursor()

sql = "DELETE FROM EMPLOYEE WHERE EMPNO = %s"

cursor.execute(sql, (1001,))
connection.commit()

print("Number of employees deleted:", cursor.rowcount)

cursor.close()
connection.close()
```

**Explanation:**

- `DELETE FROM EMPLOYEE` removes records.
- `WHERE EMPNO = %s` selects the employee to delete.
- `(1001,)` is a tuple containing one parameter. The comma is required for a single-element tuple.
- `commit()` saves the deletion.

**Warning:** Always check the `WHERE` condition. A `DELETE` statement without a `WHERE` clause can delete every row in the table.

---

## 09. Retrieve a Single Employee Record

### Q7. Write a Python program that retrieves one employee record.

**File:** `retrieveemployee.py`

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="empdb"
)

cursor = connection.cursor()

sql = "SELECT * FROM EMPLOYEE WHERE EMPNO = %s"

cursor.execute(sql, (1001,))
emprecord = cursor.fetchone()

if emprecord is not None:
    print("Employee details:")
    print("EMPNO:", emprecord[0])
    print("NAME:", emprecord[1])
    print("SALARY:", emprecord[2])
else:
    print("Employee not found.")

cursor.close()
connection.close()
```

**Explanation:**

- `SELECT` retrieves data.
- `fetchone()` returns one record.
- The returned record is typically a tuple.
- `emprecord[0]`, `emprecord[1]`, and `emprecord[2]` access the employee number, name, and salary.
- `fetchone()` returns `None` if no record matches, so the program checks before accessing the fields.

---

## 10. Retrieve Multiple Employee Records

### Q8. Write a Python program that retrieves all employee records.

**File:** `retrieveemployees.py`

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="empdb"
)

cursor = connection.cursor()

sql = "SELECT * FROM EMPLOYEE"

cursor.execute(sql)
emprecords = cursor.fetchall()

for emprecord in emprecords:
    print(
        "EMPNO:", emprecord[0],
        "NAME:", emprecord[1],
        "SALARY:", emprecord[2]
    )

cursor.close()
connection.close()
```

**Explanation:**

- `fetchall()` retrieves all remaining records returned by the query.
- The `for` loop processes each employee record.
- Each record contains the employee number, name, and salary.

If the query returns no records, `fetchall()` returns an empty list.

---

## 11. Insert Multiple Employee Records from Keyboard Input

### Q9. Write a Python program that stores multiple employee records by accepting data from the keyboard.

**File:** `storeemployees.py`

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="empdb"
)

cursor = connection.cursor()

query = """
    INSERT INTO EMPLOYEE (EMPNO, NAME, SALARY)
    VALUES (%s, %s, %s)
"""

try:
    for i in range(2):
        empno = int(input("Enter employee number: "))
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))

        cursor.execute(query, (empno, name, salary))

    connection.commit()
    print("Employees stored successfully.")

except (mysql.connector.Error, ValueError) as error:
    connection.rollback()
    print("Unable to store employees:", error)

finally:
    cursor.close()
    connection.close()
```

**Explanation:**

1. The loop runs twice, so the program accepts two employee records.
2. `input()` reads the values from the keyboard.
3. `int()` converts the employee number to an integer.
4. `float()` converts the salary to a numeric value.
5. `execute()` inserts each employee using parameterized SQL.
6. `commit()` saves both records after successful insertion.
7. `rollback()` undoes the transaction if a handled error occurs.
8. `finally` closes the cursor and connection.

### Why use `%s` placeholders?

```python
cursor.execute(query, (empno, name, salary))
```

The connector safely binds the supplied values to the SQL statement. This is preferable to building SQL by concatenating user input into a query.

---

## 12. Important Methods Summary

| Method or property | Purpose |
|---|---|
| `mysql.connector.connect()` | Connect to MySQL |
| `connection.cursor()` | Create a cursor |
| `cursor.execute()` | Execute an SQL statement |
| `connection.commit()` | Save transaction changes |
| `connection.rollback()` | Undo uncommitted transaction changes |
| `cursor.fetchone()` | Retrieve one row |
| `cursor.fetchall()` | Retrieve all remaining rows |
| `cursor.rowcount` | Get the number of affected rows |
| `cursor.close()` | Close the cursor |
| `connection.close()` | Close the connection |

## 13. Quick Revision

- **CRUD** means Create, Read, Update, and Delete.
- A **connection object** communicates with the database.
- A **cursor object** executes SQL and accesses query results.
- Use `commit()` to save changes from insert, update, and delete operations.
- Use `fetchone()` to retrieve one row and `fetchall()` to retrieve multiple rows.
- Use parameterized queries to handle values safely.
- Close database resources after completing the operations.