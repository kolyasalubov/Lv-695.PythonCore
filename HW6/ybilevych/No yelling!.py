def filter_words(st):
    text = st.capitalize().split()
    text_1 = ' '.join(text)
    return text_1

print(filter_words('HELLO world!'))