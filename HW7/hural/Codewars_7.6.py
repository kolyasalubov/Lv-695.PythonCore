#Consider an array/list of sheep where some sheep may be missing from their place.
def count_sheeps(sheep):
    return sheep.count(True)

#one more solution
def count_sheeps(array_of_sheeps):
    amount = 0
    for sheep in array_of_sheeps:
        if (sheep == True):
            amount += 1
    return amount