my_str=list(input("Enter your string:"))
def characters(my_str):
    """This function returns number of characters in the string."""
    my_str2=set(my_str)
    d={}
    for symb in my_str2:
        d[symb]=my_str.count(symb)
    return d
print(characters(my_str))
