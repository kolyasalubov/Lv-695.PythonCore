from tracemalloc import start


def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]

print(reverse_list([1,2,3,4,5,6,7]))