def my_def(word):
    my_dict = {}
    for key in word:
        if my_dict.get(key):
            my_dict[key] += 1
        else:
            my_dict[key] = 1
    return my_dict


print(my_def('hello'))
