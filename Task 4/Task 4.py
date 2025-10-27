# This entire file will be ignored by Pylint. pylint: skip-file

"""დაწერეთ პროგრამა, რომელიც იღებს სტრიქონს, როგორც შეყვანას და აბრუნებს True-ს,
თუ ის პალინდრომია (პალინდრომი არის ისეთი ტექსტი, რომელიც მარცხნიდანაც და მარჯვნიდანაც ერთნაირად იკითხება),
თუ არა მაშინ False. მაგალითად, თუ შევიყვანთ "level", ფუნქციამ უნდა დააბრუნოს True."""

user_input = ""

while user_input != "exit":
    user_input = input("შეიყვანეთ ტექსტი: ")
    reversed_text = user_input[::-1]
    if user_input == reversed_text:
        print("True")
    else:
        print("False")


"""
დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ტექსტი, 
ტექსტის სიმბოლოები გადაყავს შესაბამის ASCII სტანდარტში და გვიბეჭდავს ამ რიცხვების თანმიმდევრობას
"""

user_input_for2 = input("შეიყვანეთ ტექსტი: ")

ascii_values = [ord(char) for char in user_input_for2]

print(ascii_values)


"""
3.დაწერეთ სკრიპტი, რომელიც მომხმარებელს მოსთხოვს შეიყვანოს სიტყვა, 
შემდეგ კი შეყვანილ სიტყვას ბოლოში დაუმატებ ing-ს. თუკი მომხმარებლის მიერ
შეყვანილი სიტყვა ისედაც მთავრდება ing-ზე - მაშინ დაუმატებს ly-ს.
მაგალითად: თუკი მომხარებელმა შეიყვანტა სიტყვა test; - უნდა დაიბეჭდოს testing;
თუკი შეიყვანა string; - უნდა დაიბეჭდოს stringly ჩაწერეთ ეს while loop-ში და იყოს
გაშვებული მანამ სანამ მომხმარებელი არ ჩაწერს stop-ს
"""


while True:
    user_input_for3 = input("შეიყვანეთ ტექსტი: ")
    if user_input_for3[-3:] == "ing":
        print(user_input_for3 + "ly")
    elif user_input_for3.lower() == "stop":
        break
    else:
        print(user_input_for3 + "ing")
