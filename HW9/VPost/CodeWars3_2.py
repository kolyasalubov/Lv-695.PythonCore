def list_animals(animals):
    list = ''
    for i,animal in enumerate(animals):
        list += str(i + 1) + '. ' + animal + '\n'
    return list