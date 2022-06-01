key=True
while key:
    a=input("Enter a four-digit integer number:")
    if a.isdigit() and len(a)==4:
        key=False
    else:
        print("Data format error!")
i=0
product_of_digits=1
sort_digits=list()
while i<len(a):
    product_of_digits*=int(a[i])
    sort_digits.append(int(a[i]))
    i=i+1
print(f"The product of digits is {product_of_digits}.")
j=len(a)
reverse_number=str()
while j>0:
    reverse_number+=str(a[j-1])
    j=j-1
print(f"The reverse number is {reverse_number}.")
print(f"Digits are sorted in ascending order: {sorted(sort_digits)}.")
print (f"Digits are sorted in descending order: {sorted(sort_digits,reverse=True)}.")
