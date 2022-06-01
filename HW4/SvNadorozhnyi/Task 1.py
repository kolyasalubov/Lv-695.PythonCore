enter_number = int(input("Input a number to compute the factiorial: "))
factorial = 1

if enter_number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif enter_number == 0 or enter_number == 1:
    print(f"The factorial of {enter_number} is 1")
else:
    for i in range(2, enter_number + 1):
        factorial *= i
    print(f"The factorial of {enter_number} is {factorial}")
