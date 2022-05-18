size = input('Please enter a size of your list (a natural number): ')

if size.isdecimal() and int(size) != 0:
    size = int(size)
    list_of_elements = []
    
    print('Enter values of your list elements (only natural numbers accepted):')
    i = 0
    while i < size:
        element = input(f'Element {i+1}: ')
        if element.isdecimal():
            list_of_elements.append(int(element))
            i += 1
        else:
            print('Oops! The entered value is not an integer. Please re-enter it.')
    print()

    print('=== You have entred the following list ===')
    print(list_of_elements)   
    for i in range(size):
        list_of_elements[i] = float(list_of_elements[i])
    print()
    
    print('=== The list after convertion ===')
    print(list_of_elements)
else:
    print()
    print('Oops!!! The entered value is not a natural number.')
    print('Please launch this code again.')