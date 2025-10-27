# This entire file will be ignored by Pylint. pylint: skip-file


"""1. შექმენი ლექსიკონი classroom, სადაც ინახება სტუდენტების ინფორმაცია:
{
"student1": {"name": "ანა", "age": 20, "grade": 9},

"student2": {"name": "ნიკო", "age": 22, "grade": 8},

"student3": {"name": "მარიამ", "age": 21, "grade": 10}
}
ა) დაბეჭდე თითოეული სტუდენტის სახელი და ქულა

ბ) იპოვე სტუდენტი, ვისაც ყველაზე მაღალი ქულა აქვს

გ) დაამატე ახალი სტუდენტი "student4" შენი მონაცემებით"""

classroom = {
    "student1": {"name": "ანა", "age": 20, "grade": 9},
    "student2": {"name": "ნიკო", "age": 22, "grade": 8},
    "student3": {"name": "მარიამ", "age": 21, "grade": 10},
}

for student in classroom.values():
    print(student["name"], student["grade"])

top_student = [0, ""]

for student in classroom.values():
    if student["grade"] > top_student[0]:
        top_student = [student["grade"], student["name"]]


classroom["student4"] = {"name": "გიორგი", "age": 23, "grade": 7}

print(top_student)

"""
დაწერე პროგრამა, რომელიც ითვლის რამდენჯერ ჩნდება თითოეული სიტყვა მოცემულ ტექსტში:

მაგალითად: text = "python is great and python is easy"
"""

text = "python is great and python is easy"

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
