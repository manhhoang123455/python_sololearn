class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Gr....")

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Cat("Fido", "brown")

print(fido.name)

fido.bark()
        