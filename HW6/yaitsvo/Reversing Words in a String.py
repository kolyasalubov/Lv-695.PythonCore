def reverse(st):
    new_s = st.split()
    st = ' '.join(new_s[::-1])
    return st
print(reverse('Hi There.'))