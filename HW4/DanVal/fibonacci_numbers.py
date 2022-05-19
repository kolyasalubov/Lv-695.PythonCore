number = int(input("Input number for Fibonacci sequence\n"))
first = 0
second = 1

for __ in range(number-1):
    first, second = second, first + second
    
print(f"The {number} for Fibonacci sequence - {first}")
