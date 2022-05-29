def God():
    return (Man(), Woman())

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self):
        super().__init__(self)        
   
class Woman(Human):
    def __init__(self):
        super().__init__(self)
