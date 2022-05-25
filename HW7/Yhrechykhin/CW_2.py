def solution(number):
    total = []
    for i in range(number):
        if (i % 3 == 0 or i % 5 == 0) and i < number and i > 0:
            total.append(i)
    return sum(total)

print(solution(8))