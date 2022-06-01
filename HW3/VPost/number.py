import functools
import operator

number = input("Введите 4-ех значное число: ")

list = [int(x) for x in str(number)]
mul = functools.reduce(operator.mul,list)
print("Умножение: ", mul)

reverse = (int(str(number[::-1])))
print("Реверс:", reverse)

sort = sorted(number)
print("Сортировка:", sort)