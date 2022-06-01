import math


num = "1 3 7 5 "
list1 = num.split()
map_object = map(int, list1)
list_of_int = list(map_object)
print(list_of_int)
result1 = math.prod(list_of_int)
print(result1)
list_of_int.reverse()
print(list_of_int)
list_of_int.sort()
print(list_of_int)
