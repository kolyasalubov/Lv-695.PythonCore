string = 'Hi There.'


def reverse(st):
    # Your Code Here
    return ' '.join(st.split()[::-1])


print(reverse(string))
