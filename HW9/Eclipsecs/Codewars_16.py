def list_animals(animals):
    lists = ""
    for i in animals:
        lists += f"{animals.index(i) +  1}. {i}\n"
    return lists
