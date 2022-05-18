from random import randint
def largest_number(*args):
    """function that returns the largest number of numbers"""
    massiv = [i for i in args]
    return print(f' largest number of {massiv} is {max(massiv)}')
n = [randint(0, 100) for i in range(2)]
largest_number(*n)

