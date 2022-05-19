print("even numbers that are divisible by 2 -", [x for x in range(1,10) if x%2 == 0])

print("odd numbers that are divisible by 3 -", [x for x in range(1,10) if (x%3 == 0)and(x%2 == 1)])

print("numbers that are not divisible by 2 and 3 -", [x for x in range(1,10) if (x%3 != 0)and(x%2 != 0)])