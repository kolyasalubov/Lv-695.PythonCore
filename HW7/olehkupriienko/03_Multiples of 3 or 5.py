n = -5


def solution(num):
    total = [i for i in range(1, num) if i % 3 == 0 or i % 5 == 0]
    return sum(total)


print(solution(n))
