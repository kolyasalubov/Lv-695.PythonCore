def largest_count(x,y):
    if x == y:
        return f"digits equals"
    elif x > y:
        return x
    else:
        return y

print(largest_count(15,15))