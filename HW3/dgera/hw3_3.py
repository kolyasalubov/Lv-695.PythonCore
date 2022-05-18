value_1st = input('Please enter the 1st value: ')
value_2nd = input('Please enter the 2nd value: ')

value_1st += value_2nd
value_2nd = value_1st[0:len(value_1st) - len(value_2nd)]
value_1st = value_1st[len(value_2nd):]

# value_1st, value_2nd = value_2nd, value_1st

print('\n*** The entered values have been switched ***')
print(f'The 1st value is "{value_1st}"')
print(f'The 2nd value is "{value_2nd}"')