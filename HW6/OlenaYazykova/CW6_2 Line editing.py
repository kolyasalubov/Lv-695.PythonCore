st=input("Enter a string:")
def filter_words(st):
    return " ".join(st.capitalize().split())
print(filter_words(st))