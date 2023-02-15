class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(
            f"Hi, my name is {self.name}, I'm {self.age} years old and I live in {self.address}.")

    def greet(self):
        print("Hi friends!")


class Student(Person):
    def __init__(self, name, age, address, university):
        self.name = name
        self.age = age
        self.address = address
        self.university = university

    def introduce(self):
        print(
            f"Hi, my name is {self.name}, I'm {self.age} years old, I live in {self.address} and attend {self.university} university")


Karl = Person("Karl", 34, "L.A.")

Karl.greet()
Karl.introduce()

Jane = Student("Jane", 19, "L.A.", "UCLA")

Jane.introduce()
