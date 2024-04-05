class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello My Name is {self.name}.\nI am  {self.age} years old and my gender is {self.gender}.")

person = Person("Kelvin Githua", 22, "Male")

person.introduce()