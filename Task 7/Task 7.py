# This entire file will be ignored by Pylint. pylint: skip-file

"""დაწერეთ პროგრამა რომელიც შეადარებს ორ სეტს ერთმანეთთან და დაგვიბრუნებს ერთმანეთისგან განსხვავებულ მონაცემს"""


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}


# print(set1.symmetric_difference(set2))

"""მომხარებელმა უნდა ჩაწეროს ინფორმაცია, "helllo my name is step" და ამის შემდგომ მეორეჯერ რაიმე სხვა მონაცემი.

ორივე წინადადებაში საერთო სიტყვები და განსხვავებული სიტყვები"""

# user_input1 = set(input("Enter first sentence: ").lower().split())
# user_input2 = set(input("Enter second sentence: ").lower().split())

# print(user_input1.symmetric_difference(user_input2))
# print(user_input1.intersection(user_input2))

"""შექმენით ტაპლი 5 ობიექტისგან თუ ტაპლში არსებული ობიექტი იქნება სტრინგი მაგ შემთხვევაში
დაითვალეთ რამდენი სიმბოლოსგან შედგება თუ იქნება ინტეჯერი sum ობიქეტს დაუმატეთ"""


# my_tuple = ("14", "22", "11", "15", "hello")

# total = 0

# for i in my_tuple:
#     if i.isdigit():
#         total += int(i)
#     else:
#         print(len(i))

# print(total)


"""1. დაწერეთ პითონის პროგრამა, რომელიც ცვლის tuple-ის ბოლო მნიშვნელობას სიაში.
ნიმუშების სია: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]"""

tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_list = []

for i in tuples:
    temp_list = list(i)
    temp_list[-1] = 14
    new_list.append(tuple(temp_list))

print(new_list)

"""2.max და min ფუნქციის გარეშე იპოვეთ სეტში არსებული უმცირესი და უდიდესი მონაცემი."""

# set_numbers = {10, 20, 105, 5, 45, 99}

# min_number = None
# max_number = None

# for i in set_numbers:
#     if max_number is None or i > max_number:
#         max_number = i
#     if min_number is None or i < min_number:
#         min_number = i

# print(max_number)
# print(min_number)


"""3.დაწერეთ პითონის პროგრამა, რათა გამოვთვალოთ რიცხვების საშუალო მნიშვნელობა მოცემულ ტოპებში."""

# input = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

# average = []

# for i in range(len(input)):
#     sum = 0
#     for j in input:
#         sum += j[i]
#         temp_avg = sum / len(input)
#     average.append(temp_avg)

# print(average)
