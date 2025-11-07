# This entire file will be ignored by Pylint. pylint: skip-file

"""
# განსაზღვრეთ აბსტრაქტული კლასი Animal აბსტრაქტული მეთოდებით speak და move.
# განახორციელეთ კონკრეტული ქვეკლასები სხვადასხვა ცხოველებისთვის, თითოეული უზრუნველყოფს
# მეტყველებისა და მოძრაობის საკუთარ განხორციელებას.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        return "woof"

    def move(self):
        return "runs with four legs"


class Cat:
    def speak(self):
        return "meow"

    def move(self):
        return "walks gracefully"


"""
შექმენით კლასი Employee რომელსაც ექნება სახელი, თანამდებობა და ხელფასი. 
მეჯიქ მეთოდის საშუალებით __str__ და __repr__ დაბეჭდოს სხვადასხვა რამ
"""


class Employee:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"სახელი: {self.name}, პოზიცია: {self.position}, ხელფასი: {self.salary}"

    def __repr__(self):
        return f"სახელი: {self.name}, პოზიცია: {self.position}, ხელფასი: {self.salary}"


emp = Employee("გოგა", "დეველოპერი", 5000)

print(emp.__str__())
print(emp.__repr__())
