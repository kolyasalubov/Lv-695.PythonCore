dic = {}


def num_of_characters(st):

    for key in list(st):
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1


num_of_characters('Hello')

print(dic)
