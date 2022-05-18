var1=input("Enter the value of the first variable:")
var2=input("Enter the value of the second variable:")
#the first way
#var1,var2=var2,var1
#the second way
var1+=var2
var2=var1[0:len(var1)-len(var2)]
var1=var1[len(var2):]
print(f"The first variable is {var1}.")
print(f"The second variable is {var2}.")