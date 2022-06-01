def how_much(word):
    result = {}
    for i in word:
        if i in result:
            continue
        else:
            result.update({(i): word.count(i)})
    return result

