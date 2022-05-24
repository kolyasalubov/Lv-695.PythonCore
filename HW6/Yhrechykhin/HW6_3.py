def num_of_character(word):
    dict = {}
    for _ in word:
        keys = dict.keys()
        if _ in keys:
            dict[_] += 1
        else:
            dict[_] = 1
    return dict

word = input('Please enter the word: ')

print(num_of_character(word))