# This entire file will be ignored by Pylint. pylint: skip-file
"""
შექმენით ბიბლიოთეკის მართვის ფუნქცია(ები)
თქვენ უნდა შექმნათ ფუნქცია ან ფუნცქიები რომლის საშუალებითაც მომხმარებელი შეძლებს წიგნების
 დამატებას წაშლას პითონის პროგრამის შექმნა წიგნების პატარა ბიბლიოთეკის სამართავად.
 პროგრამამ უნდა მისცეს მომხმარებლებს შემდეგი მოქმედებების შესრულება:
1. წიგნის დამატება,
2. წიგნის მოძებნა ავტორის მიხედვით
3. წიგნის მოძებნა სათაურის მიხედვით ამისთვის აუცილებელია გამოიყენოთ ლექსიკონები
"""

library = {"დედაენა": "იაკობ გოგებაშვილი"}


def library_func():
    def check_book():
        if not library:
            print("ბიბლიოთეკა ცარიელია.")
        else:
            print("მიმდინარე ბიბლიოთეკა:")
            for title, author in library.items():
                print(f"წიგნი: {title.title()}, ავტორი: {author.title()}")

    def add_book():
        add_subject = input("შეიყვანეთ წიგნის სათაური: ").lower()
        add_author = input("შეიყვანეთ ავტორი: ").lower()
        if add_subject in library:
            print("ეს წიგნი უკვე არსებობს ბიბლიოთეკაში.")
        else:
            library[add_subject] = add_author
            print("წიგნი წარმატებით დაემატა ბიბლიოთეკას!")
            print(library)

    def del_book():
        del_subject = input("შეიყვანეთ წასაშლელი წიგნის სათაური: ").lower()
        if del_subject in library:
            library.pop(del_subject)
            print("წიგნი წარმატებით წაიშალა!")
            print(library)
        else:
            print("ასეთი წიგნი ბიბლიოთეკაში არ მოიძებნა.")

    def search_by_author():
        search_author = input("შეიყვანეთ ავტორი: ").lower()
        found = False
        for title, author in library.items():
            if author == search_author:
                print(f"მოიძებნა წიგნი: {title.title()}, ავტორი: {author.title()}")
                found = True
        if not found:
            print("ასეთი ავტორი ბიბლიოთეკაში არ მოიძებნა.")

    def search_by_title():
        search_title = input("შეიყვანეთ წიგნის სათაური: ").lower()
        if search_title in library:
            print(
                f"წიგნი: {search_title.title()}, ავტორი: {library[search_title].title()}"
            )
        else:
            print("ასეთი წიგნი ბიბლიოთეკაში არ მოიძებნა.")

    while True:
        ask_user = input(
            "\nაირჩიეთ ოპცია:\n"
            "1. წიგნის დამატება\n"
            "2. წიგნის წაშლა\n"
            "3. ავტორის მიხედვით ძებნა\n"
            "4. სათაურის მიხედვით ძებნა\n"
            "5. ყველა წიგნის ნახვა\n"
            "6. გამოსვლა\n"
            "შეიყვანეთ რიცხვი: "
        )

        if ask_user == "1":
            add_book()
        elif ask_user == "2":
            del_book()
        elif ask_user == "3":
            search_by_author()
        elif ask_user == "4":
            search_by_title()
        elif ask_user == "5":
            check_book()
        elif ask_user == "6":
            print("გმადლობთ, რომ გამოიყენეთ ბიბლიოთეკა!")
            break
        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")


library_func()
