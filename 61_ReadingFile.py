# 61. Reading File

import json
import csv

# Reading text file
file_path = "file/writing-file-1.txt"

try:
    with open(file=file_path, mode="r") as file:
        content = file.read()

        print(f"Content of '{file_path}':\n{content}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to read the file '{file_path}'.")


# Reading json file
file_path = "file/writing-file-3.json"

try:
    with open(file=file_path, mode="r") as file:
        content = json.load(file)

        print(f"Content of '{file_path}':\n{content}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")


# Reading CSV file
file_path = "file/writing-file-4.csv"

try:
    with open(file=file_path, mode="r") as file:
        reader = csv.reader(file)

        print(f"Content of '{file_path}':")

        for row in reader:

            print(row)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
