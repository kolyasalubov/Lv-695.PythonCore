class Human:
    def __init__(self, name, species):
        self.name = name
        self.species=species
        print(f"Hi, {name}!")

    def get_type(self):
        print(f"{self.name} is {self.species}.")
    
    @staticmethod
    def message():
        return print("Good Luck!")

name1=input("Enter you name: ")
hum1=Human(name1, 'Homosapiens')
hum1.get_type()
hum1.message()
