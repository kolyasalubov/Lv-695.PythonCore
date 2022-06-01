number = input('Please enter an integer number: ')

if number.isdecimal():
    number = int(number)
    fibo = []
    element_i = 0
    element_next = 1
    
    while element_i <= number:
        fibo.append(element_i)
        element_temp = element_i
        element_i = element_next
        element_next += element_temp
        # element_i, element_next = element_next, element_i + element_next
    
    print(f'=== Fibonacci sequence up to number {number} ===')
    print(fibo)
else:
    print()
    print('Oops! The entered value is not an number.')
    print('Please launch this code again.')