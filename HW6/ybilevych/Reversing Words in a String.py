def reverse(st):
    # Your Code Here
    st = st.split()
    st.reverse()  
    return ' '.join(st)

print(reverse('Hello World'))