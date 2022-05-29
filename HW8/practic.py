try:
    a=eval(int(input ("Enter a number:")))
    b=eval(int(input("enter a number:")))
    c=a/b
    print(c)
except ValueError as e:
    print("ValueError",e)

except SyntaxError as e:
    print("SyntaxError",e)  

else:
    print("")