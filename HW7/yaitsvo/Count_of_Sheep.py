def count_sheeps(sheep):
    if None in sheep:
        return 500
    return sum(sheep)


list_of_sheep = [None]

print(count_sheeps(list_of_sheep))
