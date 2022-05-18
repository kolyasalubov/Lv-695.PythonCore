# n = input('Input the n = ')
#
# if not n.isdigit():
#     print('You inputted the wrong number!')
# elif int(n) < 0:
#     print('You inputted the wrong number!')
# elif int(n) == 0:
#     print(f"Print Fibonacci numbers up to {n}: {n}")
# else:
#     result = [0, 1]
#     while int(n) >= (result[-1] + result[-2]):
#         result.append(result[-1] + result[-2])
#     print(f"Print Fibonacci numbers up to {n}: {' '.join(str(i) for i in result)}")

fibonachi_numbs = int(input("Write last numb of 'fibonachi numbers': "))
count = 1
fib_help = 1

print(count, fib_help, end=" ")
while fibonachi_numbs > 2:
    count, fib_help = fib_help, count + fib_help
    print(fib_help, end="  ")
    fibonachi_numbs -= 1