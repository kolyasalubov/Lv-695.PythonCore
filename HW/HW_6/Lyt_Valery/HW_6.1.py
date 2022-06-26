def my_comparison(number_1, number_2):
    """
    This function do comparison between 2 numbers
    """
    if number_1 > number_2:
        return number_1
    elif number_1 < number_2:
        return number_2
    else:
        return f"They are the same {number_1}"


print(my_comparison(input(), input()))
