# Python Important Notes

## 01. `globals()` Function — Run a Class by Its Name

### What is `globals()`?

The `globals()` function returns a dictionary containing the names available in the global scope of the current Python module.

We can use it to access a class or function by its name stored as a string.

### Example

```python
class Ak:
    def val(self):
        print("Ak class method executed!")

# Take the class name from the user
text = input("Enter class name: ")

# Get the class using globals()
classname = globals()[text]

# Create an object and call its method
obj = classname()
obj.val()
```

**Output:**

```text
Enter class name: Ak
Ak class method executed!
```

### How does it work?

1. `input()` takes the class name from the user as a string.
2. `globals()[text]` looks up that name in the global namespace.
3. `classname()` creates an object of the selected class.
4. `obj.val()` calls the class method through the object.

### Real-life use case

Suppose an application has multiple classes, and the user must select which operation to run. You can use a class name to select the corresponding class dynamically.

### Important: Handle invalid class names

If the user enters a class name that does not exist, `globals()[text]` raises a `KeyError`.

```python
class Ak:
    def val(self):
        print("Ak class method executed!")


text = input("Enter class name: ")

if text in globals() and isinstance(globals()[text], type):
    obj = globals()[text]()
    obj.val()
else:
    print("Class not found!")
```

**Note:** Use `globals()` carefully. It can access many global names, not just your classes. For a safer and more controlled approach, use a dictionary that explicitly maps allowed names to classes.

```python
class Ak:
    def val(self):
        print("Ak class method executed!")


class Shiv:
    def val(self):
        print("Shiv class method executed!")


classes = {
    "Ak": Ak,
    "Shiv": Shiv
}

text = input("Enter class name: ")

if text in classes:
    obj = classes[text]()
    obj.val()
else:
    print("Invalid class name!")
```

**Key takeaway:** `globals()[name]` can retrieve a globally defined class by its string name. A dictionary mapping is generally preferable when you want to allow users to select only specific classes.

## 02. Create and Activate a Virtual Environment

### What is a virtual environment?

A **virtual environment** is an isolated Python environment for a project. It helps keep project dependencies separate from other Python projects.

For example, one Django project can use Django 5.x while another project uses a different version.

### Step 1: Install `virtualenv` (optional)

You can install the `virtualenv` package using:

```bash
pip install virtualenv
```

**Note:** Installing `virtualenv` is optional. Python already includes the built-in `venv` module, which you can use without installing anything extra.

### Step 2: Create a virtual environment

Open Command Prompt or PowerShell and run:

```bash
python -m venv Akash
```

- `python -m venv` creates a virtual environment.
- `Akash` is the name of the environment folder.

For example, if you run this command from `C:\python`, your environment will be created at:

```text
C:\python\Akash\
```

### Step 3: Activate the virtual environment on Windows

**Using Command Prompt (CMD):**

```bat
C:\python\Akash\Scripts\activate.bat
```

Or, navigate to your project folder and run:

```bat
Akash\Scripts\activate.bat
```

**Using PowerShell:**

```powershell
.\Akash\Scripts\Activate.ps1
```

After activation, your terminal prompt should show the environment name:

```text
(Akash) C:\python>
```

### Step 4: Install Django inside the environment

After activating the environment, install Django:

```bash
python -m pip install django
```

Verify the installation:

```bash
python -m django --version
```

### Step 5: Deactivate the environment

To leave the virtual environment, run:

```bash
deactivate
```

You do not need to run `deactivate.bat`; `deactivate` is the standard command provided by the activated environment.

### Step 6: Activate an existing environment

If the environment already exists, activate it instead of creating it again.

For a Windows project folder named `akash`:

```bat
akash\Scripts\activate.bat
```

For macOS or Linux, the activation command is different:

```bash
source akash/bin/activate
```

**Important:** `source akash/Scripts/activate` is not the standard Windows activation command. On Windows, use `Scripts\activate.bat` in CMD or `Scripts

## 03. Install Python on Windows

### Step 1: Check the Python version

Open Command Prompt (CMD) or PowerShell and run:

```bash
python --version
```

You can also check using:

```bash
py --version
```

If Python is installed and configured correctly, you will see a version number, for example:

```text
Python 3.11.9
```

### Step 2: Download Python

1. Visit the official website: https://www.python.org/downloads/
2. Download a suitable current Python version for Windows.
3. Open the downloaded `.exe` installer.

### Step 3: Install Python

1. Run the downloaded installer.
2. Select **Install Now** for the standard installation.
3. Before installing, select the checkbox **Add python.exe to PATH** if it is available.
4. Click **Install Now** and wait for the installation to finish.

**Important:** If you already have an older Python version installed, you do not always need to uninstall it. Multiple Python versions can coexist. Choose the version you need and verify which one your terminal uses.

### Step 4: Understand the installer options

- **Add python.exe to PATH:** Allows you to run Python from CMD or PowerShell without entering its full installation path.
- **Disable path length limit:** This option may appear after installation. It allows Windows applications to use longer file paths. It is optional and is not the same as adding Python to PATH.

### Step 5: Verify the installation

Close and reopen your terminal, then run:

```bash
python --version
pip --version
```

If you have multiple Python versions installed, you can list versions registered with the Python launcher using:

```bash
py --list
```

---

## 04. Set Python Environment Variables Manually

If Python is installed but the `python` command is not recognized, you may need to configure the `Path` environment variable.

### Step 1: Open Environment Variables

1. Right-click **This PC** or **My Computer**.
2. Select **Properties**.
3. Open **Advanced system settings**.
4. Click **Environment Variables**.

On some Windows versions, you can search for **Edit the system environment variables** from the Start menu to reach the same settings.

### Step 2: Edit the Path variable

Under **User variables** or **System variables**:

1. Select the `Path` variable.
2. Click **Edit**.
3. Click **New**.
4. Add the Python installation folder.
5. Click **New** again and add the Python `Scripts` folder.
6. Click **OK** to save your changes.

### Step 3: Add the two paths

Example paths for a Python 3.11 installation:

**1. Python installation folder**

```text
C:\Users\ADMIN\AppData\Local\Programs\Python\Python311
```

**2. Python Scripts folder**

```text
C:\Users\ADMIN\AppData\Local\Programs\Python\Python311\Scripts
```

Your actual paths may be different. Use the folders where Python is installed on your computer.

### Step 4: Verify the PATH configuration

Open a new terminal and run:

```bash
python --version
pip --version
```

To see which Python executable Windows finds, run:

```bat
where python
```

**Tip:** Prefer editing the **User Path** when configuring Python just for your account. Editing the **System Path** affects all users and may require administrator permissions.

---

## 05. Create a Python Virtual Environment

A virtual environment keeps a project's Python packages separate from packages used by other projects.

### Step 1: Open your project folder

```bat
cd C:\python
```

### Step 2: Create the environment

```bash
python -m venv Akash
```

This creates an environment named `Akash` inside `C:\python`.

### Step 3: Activate the environment

For Windows Command Prompt:

```bat
Akash\Scripts\activate.bat
```

For Windows PowerShell:

```powershell
.\Akash\Scripts\Activate.ps1
```

After activation, the terminal prompt should show the environment name:

```text
(Akash) C:\python>
```

### Step 4: Install packages

For example, to install Django inside the activated environment:

```bash
python -m pip install django
```

### Step 5: Deactivate the environment

```bash
deactivate
```

**Remember:** You only need to create the environment once. Activate it whenever you work on that project.