class Human:
    @staticmethod
    def message():
        return 'london is the capital of great Britain'

    @classmethod
    def homosapiens(cls):
        return 'Homosapiens',cls

    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print("HI, {}!".format(self.name))

a = Human("Maks")
a.say_hi()
print(a.message())
print(a.homosapiens())



