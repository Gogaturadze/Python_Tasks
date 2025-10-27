# This entire file will be ignored by Pylint. pylint: skip-file

"""
დაწერეთ პროგრამა, რომელიც ჯერ csv ფაილში ჩაწერს მონაცემებს, first_name, last_name, age
# შემდეგ წაიკითხეთ ეს ფაილი, დაასორტირეთ ასაკის მიხედვით და ჩაწერეთ ახალ ფაილში
"""

import csv

data = [
    {"first_name": "John", "last_name": "Doe", "age": 28},
    {"first_name": "Jane", "last_name": "Smith", "age": 22},
    {"first_name": "Alice", "last_name": "Johnson", "age": 35},
]


with open("Task 12/people.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "age"])
    writer.writeheader()
    writer.writerows(data)


with open("Task 12/people.csv", mode="r") as file:
    reader = csv.DictReader(file)
    sorted_data = sorted(reader, key=lambda row: int(row["age"]))

with open("Task 12/sorted_people.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "age"])
    writer.writeheader()
    writer.writerows(sorted_data)
