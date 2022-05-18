test = 'hello'
# test = 'hello  / ~!'


def calc_numbers_of_char(string):

    # additional conditions for training
    # result = {i: string.lower().count(i) if i.isalpha() else 'not alfa' for i in string.lower()}
    # result = {i: string.lower().count(i) for i in string.lower() if i.isalpha()}

    result = {i: string.lower().count(i) for i in string.lower()}
    return result


print(calc_numbers_of_char(test))
