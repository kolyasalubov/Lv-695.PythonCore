class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info=f"{name}s age is {age}"
        print(self.info)
        
person1 = Person("Max",18)
person2 = Person("Olga", 20)