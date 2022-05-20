import re

password=input("Enter password: ")
res_small_let=re.findall('[a-z]',password)
res_cap_let=re.findall('[A-Z]',password)
res_numb=re.findall('[0-9]',password)
res_special_char=re.findall('[$,#,@]',password)

def res_len(password:str) ->bool:
    """Checks the length of password"""

    if len(password)>=6 and len(password)<=16:
        return True
    else:
        return False

if res_small_let and res_cap_let and res_numb and res_len(password) and res_special_char:
    print("This password is strong")
else:
    print(f"""Your password is not strong.\n
    Password must be 6 to 16 characters long,\n
    contain at least one small and one capital letter,\n
    at least one number and one special character ($ # @).
    """)