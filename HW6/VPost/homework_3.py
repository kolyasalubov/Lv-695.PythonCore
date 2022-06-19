import collections

string = str(input("Введите строку:"))

count_dict = dict(collections.Counter(string))
print(count_dict)