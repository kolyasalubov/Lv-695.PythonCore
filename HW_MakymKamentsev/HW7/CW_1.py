def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        pl_list = []
        min_list = []
        count_list = []

        for i in arr:
            if i < 0:
                min_list.append(i)
            elif i > 0:
                pl_list.append(i)

    count_list.append(len(pl_list))
    count_list.append(sum(min_list))
    return count_list
