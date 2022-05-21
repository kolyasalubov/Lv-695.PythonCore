def largest_num(x,y):
    """ This function can returns 
    the largest number of two numbers """
    if x != y:
        return max(x,y)
    else:
        return('These numbers are equal')
    
x = int(input('Please enter first number: '))
y = int(input('Please enter second number: '))
print('The largest num is',largest_num(x,y))