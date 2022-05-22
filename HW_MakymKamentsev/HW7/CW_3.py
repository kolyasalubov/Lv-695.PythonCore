def solution(number):
    summa = 0
    for i in range(number):
        if i % 3 == 0 and i %5 ==0:
            summa += i
            print("HI", i)
        elif i % 5 ==0:
            summa += i
            print("/5", i)
        elif i % 3 ==0:
            summa += i
            print("/3", i)
    return summa