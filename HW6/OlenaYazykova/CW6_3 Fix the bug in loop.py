n=float(input("Enter the number of array elements:"))
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i+=1
    return res
print(create_array(n))
