def largest_number(*args):
    """
    This function return largest number.
    Function does not have a validation of data.
    Works with any number of numbers
    """
    if not len(args):
        return f"Function must have any data. Input data."
    return max(map(str, args), key=lambda x: len(x))

# print(largest_number(123,4455,6666,1111111, 1010, 'rrrrrrrrrrr'))
# print(largest_number())
