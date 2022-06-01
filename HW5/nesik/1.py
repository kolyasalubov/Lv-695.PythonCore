print(
    f'Even numbers which are divisible by 2 - {[x for x in range(1, 11) if x%2 == 0]}')

print(
    f'Odd numbers which are divisible by 3 - {[x for x in range(1, 11) if x%3 == 0 and x%2 != 0]}')

print(
    f'Numbers which are not divisible by 2 and 3 - {[x for x in range(1, 11) if x%3 != 0 and x%2 != 0]}')
