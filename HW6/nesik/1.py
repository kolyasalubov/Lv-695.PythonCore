frst_num = float((input("Enter the first number: ").strip()))
second_num = float((input("Enter the second number: ").strip()))


def max_num(num1: float, num2: float) -> float:
    '''
    A function that calculates 
    and returns a larger number

    '''
    if num1 > num2:
        return f'The largest number is {num1}'
    else:
        return f'The largest number is {num2}'


print(max_num(frst_num, second_num))
