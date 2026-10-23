
from pathlib import Path

# Dedicated folder for files
folder = Path("uploaded_files")
folder.mkdir(exist_ok=True)


def createfile(fileName, fileContent):
    location = folder / f"{fileName}.txt"
    # location = f"uploaded_files/{fileName}.txt"

    with open(location, "w", encoding="utf-8") as file:
        file.write(fileContent)

    print(f"File created successfully: {location}")


def readFile(fileName):
    location = folder / f"{fileName}.txt"

    if location.exists():
        with open(location, "r", encoding="utf-8") as file:
            data = file.read()
            print("File data:", data)
    else:
        print("File does not exist!")

# get all files name from uploaded_files folder & store into fileName list
fileName = [];
files = folder.iterdir()
for file in files:
    if file.is_file():
        fileName.append(file.name)

action = input("What do you want to do with this file [write, read]: ")

if action.lower() == "read":
    print("Available file names: ", fileName)
    fileName = input("Enter file name without .txt: ")
    readFile(fileName)

elif action.lower() == "write":
    fileName = input("Enter file name without .txt: ")
    content = input("Enter the file content: ")
    createfile(fileName, content)

else:
    print("Please enter a valid action!")
