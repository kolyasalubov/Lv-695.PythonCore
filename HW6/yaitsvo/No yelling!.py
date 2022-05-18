def filter_words(st):
    stroka = st.capitalize().split()
    new_s = ' '.join(stroka)
    return new_s


st = 'HELLO world!'
print(filter_words(st))
