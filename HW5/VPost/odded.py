for i in range(1, 10):
    if(i % 2 == 0):
        print("Even: ", i)
    elif(i % 3 == 0):
        print("Odd numbers, which are divisible by 3: ", i)
    elif((i % 2 != 0) & (i % 3 != 0)):
        print("Numbers that are not divisible by 2 and 3: ", i)