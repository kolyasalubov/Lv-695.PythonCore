class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name}")

    @classmethod
    def myClassMethod(cls):
        print("It is a species of 'Homosapiens'")

    @staticmethod
    def myStaticMethod():
        print("Goodbye")


h = Human('Valery')
h.hello()
h.myClassMethod()
h.myStaticMethod()
