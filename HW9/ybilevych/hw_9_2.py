class Human:
    def __init__(self, name):
        self.name = name

    def greating(self):
        print(f"Hello {self.name}!")

    @classmethod
    def speacies(cls):
        print("It is a species of 'Homosapiens'")

    @staticmethod
    def message():
        print("Have a good day!")


h = Human('Jack')
h.greating()
h.speacies()
h.message()
