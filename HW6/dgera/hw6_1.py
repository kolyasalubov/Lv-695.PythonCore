def max_num(num_1: float, num_2: float) -> float:
    """
    The function that returns the largest number of two numbers.
        Parameters:
            num_1: the 1st number
            num_2: the 2nd number
        Returns:
            the largest number of two
    """
    
    if num_1 > num_2:
        return num_1
    elif num_1 < num_2:
        return num_2


num_1st = float(input('Please enter the 1st number: '))
num_2nd = float(input('Please enter the 2nd number: '))

if max_num(num_1st, num_2nd) is None:
    print('=========== Result ===========')
    print('The entered numbers are equal')
else:
    print('=========== Result ===========')
    print(f'The largest number of two numbers entered above is {max_num(num_1st, num_2nd)}')
