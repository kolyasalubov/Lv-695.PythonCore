def solution(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
        elif i < 0:
            return 0

    return sum(result)