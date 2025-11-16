# This entire file will be ignored by Pylint. pylint: skip-file

# შექმენით პრინტერის კლასი როლემსაც ექნება ორი მეთოდი, ელემნტის დამატება, დაბეჭვდვა, გამოიყენეთ queue


from queue import Queue


class Printer:
    def __init__(self):
        self.queue = Queue()

    def add_item(self, element):
        self.queue.put(element)

    def print(self):
        while True:
            self.queue.get()
            print("Printing...")


printer = Printer()
printer.add_item("Document1")
printer.add_item("Document2")
printer.print()
