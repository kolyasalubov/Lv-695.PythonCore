st=input("Enter a string:")
def reverse(st):
    st=st.split()
    print(st)
    st.reverse()
    return " ".join(st)
print(reverse(st))
