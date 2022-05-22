def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count_positives = [i for i in arr if i > 0]
    sum_negatives = [i for i in arr if i < 0]
    return [len(count_positives), sum(sum_negatives)]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(arr))
