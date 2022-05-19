#Time to practice (if statement)
number=int(input('Enter number:'))
if number %2==0:
        print('even number')
else:
    print('number is odd')

#Homework1(Write a script that will calculate the factorial of the entered number  )
n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
    print('Factorial of the number is:',fact)
