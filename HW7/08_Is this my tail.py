animal = 'Fox'
tail = 'x'


def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False


print(correct_tail(animal, tail))
