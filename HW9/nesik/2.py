class Human:

    species = "Homosapiens"

    def init(self, name):
        self.name = name

    def say(self, msg):
        return f'{self.name}>>> {msg}'

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*Static*"


man1 = Human(name="Alan")
print(man1.say("Hello"))
man2 = Human("Artur")
print(man2.say("Hello"))

print(man1.get_species())
print(man2.get_species())


Human.species = "Neanderthalensis"
print(man1.get_species())
print(man2.get_species())


print(Human.grunt())
