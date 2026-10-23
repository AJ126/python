
from pathlib import Path
import shutil

# Dedicated folder for binary files
folder = Path("uploaded_files")
folder.mkdir(parents=True, exist_ok=True)


def showFiles():
    files = sorted(file for file in folder.iterdir() if file.is_file())

    if not files:
        print("No files available!")
        return []

    print("\nAvailable files:")

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")

    return files


def createFile():
    source = input("Enter the source file path: ").strip().strip('"')
    sourcePath = Path(source)

    if not sourcePath.is_file():
        print("Source file does not exist!")
        return

    destination = folder / sourcePath.name

    if sourcePath.resolve() == destination.resolve():
        print("The file is already in the destination folder!")
        return

    if destination.exists():
        print("A file with this name already exists!")
        return

    # Copy binary data without changing its contents
    shutil.copy2(sourcePath, destination)

    print(f"File copied successfully: {destination.name}")


def readFile():
    files = showFiles()

    if not files:
        return

    try:
        choice = int(input("Enter the file number to read: "))

        if choice < 1 or choice > len(files):
            print("Invalid file number!")
            return

        location = files[choice - 1]

        # Read the file in binary mode
        with open(location, "rb") as file:
            data = file.read()

        print(f"\nFile name: {location.name}")
        print(f"File size: {len(data)} bytes")
        print(f"Binary data preview: {data[:30]!r}")

    except ValueError:
        print("Please enter a valid number!")


action = input(
    "What do you want to do? [copy/read]: "
).strip().lower()

if action == "copy":
    createFile()

elif action == "read":
    readFile()

else:
    print("Please enter a valid action!")
