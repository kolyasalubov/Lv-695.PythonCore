class Human:
    def __init__(self, name):
        self.name = name

    def hy_friend(self):
        print(f"Hi, {self.name}. Nice to meet you =)")

    @classmethod
    def my_homo(cls):
        print("it is a species of Homosapiens")

    @staticmethod
    def my_static():
        print(f"Get busy living, or get busy dying")
