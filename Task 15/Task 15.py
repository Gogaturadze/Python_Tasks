# This entire file will be ignored by Pylint. pylint: skip-file

"""
შექმენით ფუნქტორი რომელიც ხარისხში აიყვანს ინტეჯერს
"""


class Square:
    def __init__(self, x):
        self.x = x

    def __call__(self, int_number):
        return int_number**self.x


square = Square(2)

# print(square(5))


"""
შექმენით ფუნქტორი რომელიც აკუმულირებას გაუკეთებს რიცხვებს. 
var(10) -> 0+10
var(20) -> 10 + 20
"""


class Accumulator:
    def __init__(self):
        self.total = 0

    def __call__(self, number):
        self.total += number
        return self.total

    def total(self):
        return self.total


num1 = Accumulator()

num1(10)
num1(20)

print(num1.total)
