
from pathlib import Path
import csv

# Dedicated folder for CSV files
folder = Path("uploaded_files")
folder.mkdir(parents=True, exist_ok=True)


def showFiles():
    files = sorted(
        file for file in folder.glob("*.csv")
        if file.is_file()
    )

    if not files:
        print("No CSV files available!")
        return []

    print("\nAvailable CSV files:")

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")

    return files


def createFile():
    fileName = input("Enter CSV file name (without .csv): ").strip()

    if not fileName:
        print("File name cannot be empty!")
        return

    location = folder / f"{fileName}.csv"

    # Prevent overwriting an existing file
    if location.exists():
        print("CSV file already exists!")
        return

    headers = ["ID", "Name", "Age"]

    with open(location, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    print(f"CSV file created successfully: {location.name}")


def readFile():
    files = showFiles()

    if not files:
        return

    try:
        choice = int(input("Enter CSV file number to read: "))

        if choice < 1 or choice > len(files):
            print("Invalid file number!")
            return

        location = files[choice - 1]

        with open(location, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            print(f"\nContents of {location.name}:")

            for row in reader:
                print(row)

    except ValueError:
        print("Please enter a valid number!")


def addData():
    files = showFiles()

    if not files:
        return

    try:
        choice = int(input("Enter CSV file number: "))

        if choice < 1 or choice > len(files):
            print("Invalid file number!")
            return

        location = files[choice - 1]

        with open(location, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")

            writer.writerow([student_id, name, age])

        print("Data added successfully!")

    except ValueError:
        print("Please enter a valid number!")


action = input(
    "Choose action [create/read/add]: "
).strip().lower()

if action == "create":
    createFile()

elif action == "read":
    readFile()

elif action == "add":
    addData()

else:
    print("Please enter a valid action!")
