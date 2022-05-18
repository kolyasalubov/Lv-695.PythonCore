number1=float(input("Enter the first number:"))
number2=float(input("Enter the second number:"))
def number_comparison(number1, number2):
    """This function returns the largest number of two numbers."""
    if number1>number2:
        return f"The largest number is {number1}."
    else:
        return f"The largest number is {number2}."
print(number_comparison.__doc__)
print(number_comparison(number1, number2))