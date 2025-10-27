# This entire file will be ignored by Pylint. pylint: skip-file

"""დაწერეთ პითონის პროგრამა ფაილში სიის შინაარსის ჩასაწერად."""

lst = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

with open("Task 11/output.txt", "w") as file:
    filewriter = file.write("\n".join(lst))


"""2. დაწერეთ ფუნქცია პითონში, ტექსტურ ფაილში მაღალი რეგისტრში არსებული

წინადადებების დასათვლელად."""


def count_uppercase(txt):
    count = 0
    for word in txt:
        if any(char.isupper() for char in word):
            count += 1
    print("მაღალ რეგისტრში დაწერილი სიტყვების რაოდენობაა:", count)


with open("Task 11/output.txt", "r") as file:
    file = file.readlines()
    count_uppercase(file)
