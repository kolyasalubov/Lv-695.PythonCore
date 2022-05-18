num = int(input('Enter a four-digit number: '))

product = 1
for i in str(num):
    product *= int(i)

reverse_num = int(str(num)[::-1])
sorted_num = ''.join(sorted(i for i in str(num)))

print('The product of the digits is:', product)
print('The number in reverse order is: ', reverse_num)
print('The sorted number is:', sorted_num)
