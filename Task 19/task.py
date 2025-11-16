# This entire file will be ignored by Pylint. pylint: skip-file

import json


class Student:
    def __init__(self, name="", age=0, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def read_json(self, file):
        with open(file, "r") as f:
            data = json.load(f)
            return data

    def average_score(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def write_json(self, old_file, new_output):
        data = self.read_json(old_file)
        students = data.get("students", [])
        result = []

        for student in students:
            grades = student.get("grades", [])
            avg = sum(grades) / len(grades) if grades else 0
            result.append({"name": student.get("name", ""), "average_score": avg})

        with open(new_output, "w") as f:
            json.dump(result, f, indent=4)


student = Student()
student.write_json("Task 19/students.json", "Task 19/students_average.json")
