#Fibonacci numbers up to the entered number n,using cycles. 
number=int(input("Enter number:"))
n1,n2 =0,1
count=0
if number<=0:
    print('Enter a number more than 0')
elif number ==1:
        print("Fibonacci number:",number)
else:
    print('Fibonacci sequence:')
    while count< number:
        print(n1)
        seq=n1+n2
        n1=n2
        n2=seq
        count += 1

       
