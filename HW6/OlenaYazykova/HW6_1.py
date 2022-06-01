number1=float(input("Enter the first number:"))
number2=float(input("Enter the second number:"))
def number_comparison(number1: float, number2: float) ->float:
    """This function returns the largest number of two numbers."""

    if number1>number2:
        return f"The largest number is {number1}."
    elif number1<number2:
        return f"The largest number is {number2}."
    else:
        return f"These numbers are equal: {number1} = {number2}"
print(number_comparison.__doc__)
print(number_comparison(number1, number2))
