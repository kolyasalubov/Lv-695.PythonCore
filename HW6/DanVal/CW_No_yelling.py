def filter_words(st):
    while "  " in st:
        st = st.replace("  ", " ").strip()
    return st.lower().capitalize()

# print(filter_words("hEEEElo wotttt      hhh  AAAAA aa     AAAAAAAAAA"))