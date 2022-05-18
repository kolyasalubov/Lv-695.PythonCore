def largest_number(first_number, second_number):
    """Returns the largest
    number of two numbers """
    if first_number > second_number:
        return f"{first_number} > {second_number}"
    elif first_number < second_number:
        return f"{first_number} < {second_number}"
    else:
        return f"{first_number} = {second_number}"


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print(largest_number(num1, num2))
print(largest_number.__doc__)
