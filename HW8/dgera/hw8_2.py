class Human():
    
    spec = 'Homosapien'
    
    def __init__(self, name: str, sex: str, age: int) -> None:
        self.name = name
        self.sex = sex
        self.age = age
    
    def welcom(self) -> None:
        print (f'Dear {self.name}, welcome on board!')

    @classmethod
    def species(cls, obj) -> str:
        return f'{obj.name} is a {cls.spec}.'
    
    @staticmethod
    def arbitary(name: str, sex: str, age: int) -> str:
        return f'{name}\'s data: {sex}, {age} years old'
    

person_1 = Human('John', 'man', 30)
person_2 = Human('Helen', 'woman', 21)
person_3 = Human('Adam', 'man', 40)

person_1.welcom()
Human.welcom(person_2)
person_3.welcom()

print('==========')
print(Human.species(person_1))
print(Human.species(person_2))
print(Human.species(person_3))

print('==========')
print(person_1.arbitary(person_1.name, person_1.sex, person_1.age))
print(Human.arbitary(person_2.name, person_2.sex, person_2.age))
print(person_3.arbitary(person_3.name, person_3.sex, person_3.age))
