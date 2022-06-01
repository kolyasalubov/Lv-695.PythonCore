def summation(num):
    return num + summation(num-1) if num > 1 else 1
