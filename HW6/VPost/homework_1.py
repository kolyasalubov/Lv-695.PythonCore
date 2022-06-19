number_1 = int(input("Введите число:"))
number_2 = int(input("Введите число:"))

def func(number_1, number_2):
    if number_1 > number_2:
        return number_1
    if number_2 > number_1:
        return number_2
    if number_1 == number_2:
        return print("Одинаковые числа")


print(func(number_1, number_2))
        

