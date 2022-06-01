my_name = 'Oleh'
my_age = 31


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{self.name} is {self.age} years old'


person1 = Person(my_name, my_age)
print(person1.info)
