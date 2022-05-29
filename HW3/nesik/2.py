# The First Task
number = (input('Enter a four-digit number: ').strip())

product = 1

for num in number:
    product *= int(num)

print(product)

# The Second Task
reverse_number = int(str(number)[::-1])
print(f'Reverse number: {reverse_number}')

# The Third Task
sorted_number = ''.join(sorted(num for num in str(reverse_number)))
print(f'Sorted number: {sorted_number}')
