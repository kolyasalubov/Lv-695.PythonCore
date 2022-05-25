def count_positives_sum_negatives(arr):
    output = []
    if arr:
        output.append(sum([1 for x in arr if x > 0]))
        output.append(sum([x for x in arr if x < 0]))
    return output

arr1 = [-88, 6, -24, 20, -26, 38, -29, -13, -60, 62, -77, 6, 88, 86, -23, -46, -87, -84, -61, 78, 44, 64, -28, 78, 24, 38, -30, 13, 69, 21, 67, -70, 21, 100, 51, -78, 70]
print(count_positives_sum_negatives(arr1))