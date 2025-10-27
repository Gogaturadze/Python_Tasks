# This entire file will be ignored by Pylint. pylint: skip-file

"""დავეწეროთ პროგრამა რომელიც a,b,c,d მეშვეობით შეაფასებს სტუდენტს.
სტუდენტი ჩაწერს int და უნდა დავაბრუნოთ ნიშანი."""


def student_grade(number):

    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    elif number >= 60:
        return "D"
    else:
        return "F"


print(student_grade(85))


"""დაწერეთ პითონის ფუნქცია რომელიც მიიღებს არგუმენტს,
პირობითად num_1 და num_2-ს შემდეგ ამის და მიხედვით შექმნის ლისტს
და საბოლოოდ დაგვიბრუნებს ლისტში არსებული ყველა ობიექტის კვადრატს"""


def num_squared(num_1, num_2):
    if num_2 < num_1:
        num_1, num_2 = num_2, num_1

    lst = [n**2 for n in range(num_1, num_2 + 1)]

    return lst


print(num_squared(5, 1))
