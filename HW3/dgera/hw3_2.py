number = input('Please enter a 4-digits natural number: ')

if len(number) == 4 and number.isdecimal() and int(number) >= 1000:
    # Subtask 1
    print(' Subtask 1 '.center(19, '='))
    mult = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
    print(f'{number[0]} * {number[1]} * {number[2]} * {number[3]} = {mult}')
    
    # Subtask 2
    print()
    print(' Subtask 2 '.center(19, '='))
    reversal_order = int(''.join(number[::-1]))
    # reversal_order = int(''.join(reversed(number)))
    print(f'{number} in reversal order: {reversal_order:04d}')
    
    # Subtask 3
    print()
    print(' Subtask 3 '.center(19, '='))
    
    sorted_asc_order=int(''.join(sorted(number)))
    print(f'{number} sorted by ascending order: {sorted_asc_order:04d}')
    
    sorted_desc_order=int(''.join(sorted(number, reverse=True)))
    print(f'{number} sorted by descending order: {sorted_desc_order:04d}')
else:
    print('Oops! The entered value is not a 4-digits natural number.')
    print('Please launch this code again.')