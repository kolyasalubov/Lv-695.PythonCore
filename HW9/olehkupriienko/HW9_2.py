class Carr:
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model

    def star(self):
        print(f'{self.kind} {self.name} {self.model} started')

    def stop(self):
        print(f'{self.kind} {self.name} {self.model} stopped')


first_car = Carr('Tesla', 'Electrical', 'Model X')
second_car = Carr('Honda', 'Hatchback', 'Civic')

first_car.star()
second_car.star()
second_car.stop()
first_car.stop()
