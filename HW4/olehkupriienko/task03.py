n = input('Input the n = ')

if not n.isdigit():
    print('You inputted the wrong number!')
elif int(n) < 0:
    print('You inputted the wrong number!')
elif int(n) == 0:
    print(f"Print Fibonacci numbers up to {n}: {n}")
else:
    result = [0, 1]
    while int(n) >= (result[-1] + result[-2]):
        result.append(result[-1] + result[-2])
    print(f"Print Fibonacci numbers up to {n}: {' '.join(str(i) for i in result)}")
