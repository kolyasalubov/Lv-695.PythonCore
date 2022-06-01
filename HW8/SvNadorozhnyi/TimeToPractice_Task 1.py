class Human:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greeting(self):
        return f"Hello {self.name}!"

    @classmethod
    def species_information(cls):
        return f"{cls} are Homosapiens"

    @staticmethod
    def my_message():
        return "check staticmethod"


human_test = Human("Taras", "Homosapiens")
print(human_test.greeting())
print(human_test.species_information())
print(human_test.my_message())
