def solution(number):
    sum = 0
    if number <= 0:
        return sum
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum
    