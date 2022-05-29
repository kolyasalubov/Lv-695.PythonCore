#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(bool):
    
    if bool==True or False:
       return print("Yes")
    if bool != True or False:
       return print("No")

bool_to_word(input())    