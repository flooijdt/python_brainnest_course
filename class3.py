class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Pet):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Bark! Bark!")


class Cat(Pet):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Meoooow!")


marta = Cat("marta")
bobby = Dog("bobby")

marta.speak()
bobby.speak()
