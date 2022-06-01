def count_positives_sum_negatives(arr):
    pos = []
    neg = []
    if arr == []:
        return arr
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
            
    return [len(pos), sum(neg)] 


print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
print(count_positives_sum_negatives([]))