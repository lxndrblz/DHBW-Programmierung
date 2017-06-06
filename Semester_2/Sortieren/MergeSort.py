def merge_sort(l1, l2):
    l_sorted = []
    counter_l1 = 0
    counter_l2 = 0
    while len(l_sorted) < len(l1) + len(l2):
        if counter_l1 < len(l1) and counter_l2 < len(l2):
            if l1[counter_l1] < l2[counter_l2]:
                l_sorted.append(l1[counter_l1])
                counter_l1 += 1
            else:
                l_sorted.append(l2[counter_l2])
                counter_l2 += 1
        else:
            if counter_l1 >= len(l1) and counter_l2 < len(l2):
                l_sorted.append(l2[counter_l2])
                counter_l2 += 1
            elif counter_l2 >= len(l2) and counter_l1 < len(l1):
                l_sorted.append(l1[counter_l1])
                counter_l1 += 1
            else:
                l_sorted.append(l1[counter_l1])
                counter_l1 += 1
                l_sorted.append(l2[counter_l2])
                counter_l2 += 1
                counter_l1 += 1

    return l_sorted


def split_list(l_to_split):
    if len(l_to_split) is 1:
        return l_to_split

    half = int(len(l_to_split) / 2)

    return merge_sort(split_list(l_to_split[:half]), split_list(l_to_split[half:]))


l_to_sort = [1, 2, 3, 4, 15, 16, 72, 81, 19, 10, 6, 13, 18]

print(split_list(l_to_sort))
