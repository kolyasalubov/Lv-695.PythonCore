def filter_words(st):
    st = st.capitalize().split()
    new_st = ' '.join(st)
    return new_st

print(filter_words('HELLO WORLD!'))