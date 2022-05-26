class Human:
    """
    Class Human
    """
    
    def __init__(self,name):
        self.name = name
        
        
    def welcome(self):
        print(f'Welcome, {self.name}')
    
    @classmethod
    def classmethod(cls):
        print("Homosapience"),cls

    @staticmethod
    def staticmethod():
        print (f'Have a nice day!')
    
t1 = Human("Max")
t1.welcome()
t1.classmethod()
t1.staticmethod()

