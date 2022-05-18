def str_count(st):
    if type(st) == type(" "):
        return {i: st.count(i) for i in st}
    else:
        print("You enter not string. Pls try again!")    

enter_w = input("Enter your string: ")
enter_l = enter_w.lower()
print(str_count(enter_l))

