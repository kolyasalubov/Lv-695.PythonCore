s=input("Enter your string: ")

def double_char(s:str) ->str:
    """This function return a string in which each character is repeated once."""

    my_list=[]
    for i in list(s):
        my_list.append(i*2)
    return ''.join(my_list)

print(double_char(s))