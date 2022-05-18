enter_fibo_number = int(input("Input a number: "))
fibo1 = 1
fibo2 = 1

while enter_fibo_number - 2 > 0:
    fibo1, fibo2 = fibo2, fibo1 + fibo2
    enter_fibo_number -= 1
    print(fibo2)