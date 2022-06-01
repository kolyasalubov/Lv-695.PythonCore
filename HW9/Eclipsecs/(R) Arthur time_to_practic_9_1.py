class Human:
    def __init__(self, name, specie = "Homosapiens"):
        self.name = name
        self.specie = specie
    
    def great(self):
        return f"Hello, {self.name}"
    
    def species(self):
        return f"You are {self.specie}"
    
    @staticmethod
    def stat():
        return "What`s up?"

hum = Human("Albert")
print(hum.great() + ". " + hum.species() + ". \n" + hum.stat())