def calculates_number_of_characters(my_str):
    my_dict = {}
    for ch in my_str:
        my_dict[ch] = my_dict.get(ch, 0) + 1
    return my_dict

# print(calculates_number_of_characters('1223334444555556666667777777'))
