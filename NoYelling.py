def filter_words(st):
    st = st.lower()
    title_st = st[0]
    st = st[1:]
    return ' '.join(str(title_st.upper() + st).split())