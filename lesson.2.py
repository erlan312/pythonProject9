class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        return f'NAME: {self.name}, AGE: {self.age}, BIRTH YEAR: {2024 - self.age}'

some_Animal = Animal('Bob', 18)
print(some_Animal.print_info())

class cat(Animal):