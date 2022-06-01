number = int(input('Enter the number: '))
factorial = 1

if number < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 = 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial = {factorial}")