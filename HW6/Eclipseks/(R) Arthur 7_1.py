def lot_back(first_num, sec_num):
    """ This function can returns the largest number of two numbers """
    if first_num == sec_num:
        print(first_num)
    elif first_num < sec_num:
        print(sec_num)
    else:
        print(first_num)

print(lot_back(8, 8))