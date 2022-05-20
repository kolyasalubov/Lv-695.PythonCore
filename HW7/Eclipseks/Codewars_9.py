def solution(number):
    dig = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
           dig.append(i) 
    return sum(dig)
