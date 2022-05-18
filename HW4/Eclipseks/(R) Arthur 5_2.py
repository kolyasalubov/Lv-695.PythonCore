fibonachi_numbs = int(input("Write last numb of 'fibonachi numbers': "))
count = 1
fib_help = 1

print(count, fib_help, end=" ")
while fibonachi_numbs > 2:
    count, fib_help = fib_help, count + fib_help
    print(fib_help, end="  ")
    fibonachi_numbs -= 1