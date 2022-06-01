class Human:
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        pass

class Woman(Human):
    def __init__(self):
        pass

def God():
    men_1=Man()
    women_1=Woman()
    return [men_1,women_1]

print(God())
