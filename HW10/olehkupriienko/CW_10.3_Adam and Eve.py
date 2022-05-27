class Human:
    pass


class Man(Human):
    def __init__(self, name):
        self.name = name


class Woman(Human):
    def __init__(self, name):
        self.name = name


adam = Man('Adam')
eve = Woman('Eve')


def god():
    print([adam.__class__, eve.__class__])
    return [adam, eve]


print(god())
