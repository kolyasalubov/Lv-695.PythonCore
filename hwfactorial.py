n=int(input("Enter the number: "))
fact=1
if n<0:
    print("factorial ")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of", n, "is", fact)
