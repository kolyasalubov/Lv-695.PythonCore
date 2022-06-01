def count_positives_sum_negatives(arr):
    if arr in ([], None):
        return []
    else:
        count_positives = 0
        sum_negatives = 0
        for num in arr:
            if num > 0:
                count_positives +=1
            elif num < 0:
                sum_negatives += num
        return [count_positives, sum_negatives]