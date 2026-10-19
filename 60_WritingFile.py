# 60. Writing File

import json
import csv

# Writing text data
txt_data = "I like pizza"

file_path = "file/writing-file-1.txt"

try:
    with open(file=file_path, mode="a") as file:
        file.write("\n" + txt_data)

        print(f"Data written to '{file_path}' successfully.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")


# Writing list of data
employees = ["John Doe", "Jane Smith", "Bob Johnson", "Alice Brown"]

file_path = "file/writing-file-2.txt"

try:
    with open(file=file_path, mode="w") as file:

        for employee in employees:
            file.write(employee + "\n")

        print(f"Data written to '{file_path}' successfully.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")


# Writing dictionary data
employee_data = {
    "name": "John Doe",
    "age": 30,
    "job": "Software Engineer",
}

file_path = "file/writing-file-3.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee_data, file, indent=4)

        print(f"Data written to '{file_path}' successfully.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")


# Writing CSV data

employee_list = [
    ["Name", "Age", "Job"],
    ["John Doe", 30, "Software Engineer"],
    ["Jane Smith", 28, "Data Analyst"],
    ["Bob Johnson", 35, "Project Manager"],
]

file_path = "file/writing-file-4.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        for row in employee_list:
            writer.writerow(row)

        print(f"Data written to '{file_path}' successfully.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")
