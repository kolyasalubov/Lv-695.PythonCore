boolean=bool(input("Enter '1' if true or '' if false: "))

def bool_to_word(boolean:bool)->str:
    """The function returns string 'yes' if variable is True and 'no' if variable is False."""

    if boolean==True:
        return f"Yes"
    else:
        return f"No"

print(bool_to_word(boolean))