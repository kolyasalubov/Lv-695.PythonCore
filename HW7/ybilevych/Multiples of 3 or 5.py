def solution(number):
    a = []
    for i in range(0, number):
        if i % 3 == 0:
            a.append(i)
        elif i % 5 == 0:
            a.append(i)
    return sum(a)

print(solution(200))
