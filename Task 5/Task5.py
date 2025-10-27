# This entire file will be ignored by Pylint. pylint: skip-file

"""2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]],
და შეასრულებს შემდეგ ნაბიჯებს: a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა b. დაამატებს
ბოლო ელემენტში ტექსტს "hello" c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს d.
შექმენით ახალი ლისტი my_llist_2"""

my_llist = [43, "22", 12, 66, 210, ["hi"]]

index_of_210 = [i for i in range(len(my_llist)) if my_llist[i] == 210]
print(index_of_210)

my_llist[-1].append("hello")

my_llist.pop(2)
print(my_llist)

my_llist_2 = my_llist.copy()

"""3. დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული 3x3 მატრიცის ტრანსპონირებას, 
ტრანსპონირება ნიშნავს ინდექსების შებრუნებას, მაგ. თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[2][3],
ტრანსპონირების შემდეგ მისი ინდექსი უნდა გახდეს list[3][2], ასე ხდება ყველა ჩანაწერზე"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])

transposed = []

for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transposed.append(new_row)

print(transposed)
