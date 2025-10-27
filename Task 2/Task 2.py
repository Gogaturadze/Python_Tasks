# დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას.
# თუ რიცხვი ლუწია გამოიტანეთ ტექსტი ‘even ’თუ კენტია ‘odd

user_input = int(input("Input number to check it's odd ro even: "))


if user_input <= 0:
    print("input number more than0")

elif (user_input % 2) == 0:
    print("even")
else:
    print("odd")

# დაწერეთ პროგრამა, რომელიც მიიღებს მოსწავლის ქულებს, როგორც შეყვანის სახით და დაბეჭდავს
# მათ შესაბამის შეფასებას (A, B, C და ა.შ.) if-elif-else ოპერატორების გამოყენებით.

student_score = int(input("Student score is ? "))

if student_score <= 60:
    score = "E"
elif student_score <= 70:
    score = "D"
elif student_score <= 80:
    score = "C"
elif student_score <= 90:
    score = "b"
else:
    score = "A"

print(f"Student score is {score}")


# დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ ტექსტში მოძებნის სიტყვებს “small”, “tall”, “middle”

user_str = input("Please type the text: ")


if "tall" in user_str.lower():
    print("tall")
elif "small" in user_str.lower():
    print("small")
elif "middle" in user_str.lower():
    print("middle")
else:
    print("tall,small and middle don't exist in the text")
