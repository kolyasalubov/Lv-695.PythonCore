num1 = int(input('Please, input first number: num1 = '))
num2 = int(input('Please, input second number: num2 = '))


def find_max_of_two_nuber(n1, n2):
    """
    Find the largest value.

    This is equivalent to Python max() function

    :param n1: arg1
    :type n1: int
    :param n2: arg2
    :type n2: int
    :rtype: int
    :return: largest of two numbers
    """

    if n1 > n2:
        largest = n1
    elif n1 < n2:
        largest = n2
    else:
        raise ValueError('There is no largest. Numbers are equal')
    return f'The largest number is {largest}'


print(find_max_of_two_nuber(num1, num2))
