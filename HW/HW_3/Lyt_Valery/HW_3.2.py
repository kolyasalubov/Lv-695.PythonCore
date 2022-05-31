number = input()

num_1 = int(number) / 1000
num_2 = int(number) % 1000 / 100
num_3 = int(number) % 100 / 10
num_4 = int(number) % 10

dobutok = int(num_1) * int(num_2) * int(num_3) * int(num_4)
print(dobutok)

array = [int(num_1), int(num_2), int(num_3), int(num_4)]

array.reverse()
print(array)

array.sort()
print(list(array))
