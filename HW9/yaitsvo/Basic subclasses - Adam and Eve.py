class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass

def God():
    Hu1 = Man()
    Hu2 = Woman()
    return [Hu1, Hu2]

print(God())