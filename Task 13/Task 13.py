# This entire file will be ignored by Pylint. pylint: skip-file

"""
დაწერეთ პითონის პროგრამა კლასების გამოყენებით, რომელიც წარმოადგენს კალათას. დაწერეთ ნივთების დამატებისა
და წაშლის მეთოდები და პროდუქტების ფასის დათვლა.
"""


class ShoppingCart:

    def __init__(self, cart=[]):
        self.cart = cart

    def add_item(self, item, quantity):
        self.cart.append((item, quantity))
        return f"ნივთი {item} დამატებულია კალათაში {quantity} რაოდენობით."

    def remove_item(self, item):
        for i in self.cart:
            if i[0] == item:
                self.cart.remove(i)
                return f"ნივთი {item} წაიშალა კალათიდან."
        else:
            f"ნივთი {item} არ მოიძებნა კალათაში."

    def calculate_total(self):
        total = 0
        for i in self.cart:
            total += i[1]
        return f"ჯამი {total} ნივთი."

    def current_items(self):
        return f"ამჟამად კალათაშია:\n{self.cart}"


cart = ShoppingCart()

cart.add_item("პური", 2)
cart.add_item("კარაქი", 1)
cart.add_item("წყალი", 6)
cart.add_item("ზეთი", 2)

print(cart.current_items())
print(cart.calculate_total())

cart.remove_item("ზეთი")
print(cart.current_items())
print(cart.calculate_total())


"""
შექმენით კლასი რომელიც იქნება Human კლასი, ატრიბუტებს გადავცემთ სახელს, გვარს, ასაკს, სიმაღლეს,
და შექმენით რამოდენიმე მეთოდი რომელიცაა, შექმენით მეთოდი რომელიც გამოიანგარიშებს ადამიანის ასაკს,
დაგვიბრუნებს ადამიანის სახელს, და დაგვიბრუნებს ადამიანის სიმაღლეს
"""


class Human:

    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def get_age(self):
        return f"თქვენი ასაკია {self.age} წელი"

    def get_name(self):
        return f"თქვენი სახელია {self.name}"

    def get_height(self):
        return f"თქვენი სიმაღლეა {self.height} სმ"


human1 = Human("გოგა", "თურაძე", 26, 173)


"""
# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount,
# ისეთი ატრიბუტებით, როგორიცაა account_number, account_holder და ბალანსი.
# ფულის ჩარიცხვისა და გამოტანის მეთოდების დანერგვა.
# შექმენით BankAccount კლასის ინსტანციები და განახორციელეთ რამდენიმე ტრანზაქცია.
"""


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} ლარი ჩარიცხულია. ახალი ბალანსი: {self.balance} ლარი."

    def withdraw(self, amount):
        if amount > self.balance:
            return "არ არის საკმარისი თანხა ანგარიშზე."
        else:
            self.balance -= amount
            return f"{amount} ლარი გამოტანილია. ახალი ბალანსი: {self.balance} ლარი."


gturadze = BankAccount("GE1234567890", "გოგა თურაძე", 1000)


"""
# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა სახელი,
# student_id და კურსები (კურსების სია, რომელშიც სტუდენტი არის ჩარიცხული).
# დანერგეთ მეთოდი სტუდენტის ინფორმაციისა და ჩარიცხული კურსების ჩვენების მიზნით.
# შექმენით სტუდენტური კლასის ინსტანციები და ჩაწერეთ ისინი სხვადასხვა კურსებზე.
"""


class Student:

    def __init__(self, name, student_id, courses=[]):
        self.name = name
        self.student_id = student_id
        self.courses = courses

    def add_course(self, course):
        self.courses.append(course)

    def info(self):
        return f"სტუდენტის სახელი: {self.name}, სტუდენტის ID: {self.student_id}, ჩარიცხული კურსები: {', '.join(self.courses)}"


student1 = Student("გოგა", "id12345", ["მათემატიკა", "ფიზიკა", "ქიმია"])

student1.add_course("ბიოლოგია")

print(student1.info())
