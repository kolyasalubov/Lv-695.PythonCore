def char_counter(stroka):
    return {i: stroka.lower().count(i) for i in stroka.lower()}
print(char_counter(input()))

