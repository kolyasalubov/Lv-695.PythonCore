class Human:
    arbitrary_message = 'What?'

    def __init__(self, name, type):
        self.name = name
        self.type = type

        print('Nice to meet you', self.name)

    def get_type(self):
        print(f'{self.name} is a species of {self.type}')

p1 = Human('Volodymyr', 'Homosapiens')
p1.get_type()
p2 = Human('Yevhen', 'Homosapiens')
p2.get_type()