# Python Commands – Complete Notes

## 1. Upgrade pip

`pip` is Python's package installer. It is used to install, upgrade, and manage Python packages.

### Command

```bash
python -m pip install --upgrade pip
```

### Explanation

- `python` runs the Python interpreter.
- `-m pip` runs pip as a Python module.
- `install` installs a package.
- `--upgrade` upgrades the specified package.
- `pip` is the package being upgraded.

To check the installed pip version:

```bash
python -m pip --version
```

**Tip:** Using `python -m pip` helps ensure pip belongs to the Python interpreter you are using.

---

## 2. Check the Python Version

Use the following commands to check the installed Python version.

```bash
python --version
```

Or:

```bash
python -V
```

Example output:

```text
Python 3.13.2
```

The actual version depends on the Python version installed on your computer.

### Windows alternatives

```bash
py --version
```

To list Python versions available through the Windows Python launcher:

```bash
py --list
```

---

## 3. Check Installed Packages

Display packages installed in the current Python environment.

```bash
python -m pip list
```

Example output:

```text
Package     Version
----------  -------
pip         25.0
requests    2.32.3
```

The output depends on the packages installed in your environment.

---

## 4. Check Outdated Packages

Identify installed packages that have newer versions available.

```bash
python -m pip list --outdated
```

This command displays information about outdated packages, including their current and latest available versions.

Example output:

```text
Package    Version    Latest
---------  ---------  --------
requests   2.30.0     2.32.3
```

This is an illustrative example, not a live package listing.

---

## 5. Upgrade a Specific Package

To upgrade one package, use:

```bash
python -m pip install --upgrade package_name
```

Example:

```bash
python -m pip install --upgrade requests
```

This asks pip to install the latest compatible version of `requests` available from the configured package index.

---

## 6. Upgrade Multiple Outdated Packages

First, check which packages are outdated:

```bash
python -m pip list --outdated
```

Then upgrade the required packages individually:

```bash
python -m pip install --upgrade requests
python -m pip install --upgrade Django
```

### Windows PowerShell option

To attempt upgrading all outdated packages in the current environment:

```powershell
python -m pip list --outdated --format=json |
    ConvertFrom-Json |
    ForEach-Object {
        python -m pip install --upgrade $_.name
    }
```

**Important:** Upgrading every package automatically can break projects because packages may depend on different versions of the same library. Use a virtual environment and test your project after upgrading.

---

## 7. Create a requirements.txt File

A `requirements.txt` file records Python package dependencies for a project.

### Command

```bash
python -m pip freeze > requirements.txt
```

### Explanation

- `pip freeze` lists installed packages in a requirements-compatible format.
- `>` redirects the command output into a file.
- `requirements.txt` is the destination file.
- If the file already exists, `>` replaces its contents.

Example contents:

```text
requests==2.32.3
Django==5.2
```

These are example entries. Your file will contain packages and versions from your environment.

**Important:** `pip freeze` records the installed environment. It does not automatically determine which packages your application actually needs.

---

## 8. Install Packages from requirements.txt

To install dependencies listed in a requirements file:

```bash
python -m pip install -r requirements.txt
```

### Explanation

- `-r` tells pip to read package requirements from a file.
- Each listed dependency is installed or satisfied according to its requirement.

### Upgrade packages using a requirements file

```bash
python -m pip install --upgrade -r requirements.txt
```

**Important:** If the file contains exact version pins, such as `requests==2.32.3`, pip will generally retain those specified versions. To upgrade dependencies to newer versions, update the requirements file or use an appropriate dependency-management workflow.

---

## 9. Create and Activate a Virtual Environment

A virtual environment keeps a project's packages separate from those of other projects.

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate in Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Activate in Windows Command Prompt

```bat
.venv\Scripts\activate.bat
```

### Deactivate the environment

```bash
deactivate
```

After activating the environment, install packages and generate `requirements.txt` for that project.

---

## 10. Recommended Workflow

For a new Python project:

1. Create a project folder.
2. Create a virtual environment.
3. Activate the environment.
4. Install the required packages.
5. Save dependencies in `requirements.txt`.
6. Use version control to track your code and dependency file.

### Example

```bat
mkdir my_python_project
cd my_python_project

python -m venv .venv
.venv\Scripts\activate

python -m pip install requests
python -m pip freeze > requirements.txt
```

### Best Practices

- Use a virtual environment for each project.
- Prefer `python -m pip` to avoid using the wrong pip installation.
- Review package upgrades before applying them to important projects.
- Keep `requirements.txt` updated when dependencies change.
- Test your project after upgrading dependencies.

---

## Quick Revision Table

| Task | Command |
|---|---|
| Check Python version | `python --version` |
| Check pip version | `python -m pip --version` |
| List installed packages | `python -m pip list` |
| List outdated packages | `python -m pip list --outdated` |
| Upgrade pip | `python -m pip install --upgrade pip` |
| Upgrade a package | `python -m pip install --upgrade requests` |
| Create virtual environment | `python -m venv .venv` |
| Save dependencies | `python -m pip freeze > requirements.txt` |
| Install dependencies | `python -m pip install -r requirements.txt` |
| Deactivate environment | `deactivate` |

