def count_positives_sum_negatives(arr):
    if not arr:
        return []
    return [len(list(filter(lambda x: x > 0, arr))), sum(list(filter(lambda x: x < 0, arr)))]
    