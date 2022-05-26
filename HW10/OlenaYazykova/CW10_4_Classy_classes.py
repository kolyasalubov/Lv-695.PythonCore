class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

person_1=Person('John', '34')
print(person_1.info)
