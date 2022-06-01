class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __get_info(self):
        return f"{self.name}s age is {self.age}"
    
    info = property(__get_info)
