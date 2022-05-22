def solution(number):
    if number <= 0:
        return 0
    return sum(set([i for i in range(number) if i % 3 == 0 or i % 5 == 0]))
print(solution(-1))