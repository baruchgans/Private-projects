def marge_2_sorted_arrays(a, b):
    # while curr_a < len a and curr_b < len b:
    #         compare curr_a VS curr_b,
    #             take the smallest and add it to new auxiliary arr,
    #             and advance the variable forward by one
    # take the rest of unfinished arr into the new arr

    if not a:
        return b
    if not b:
        return a
    curr_a = 0
    curr_b = 0
    auxiliary_arr = []
    while curr_a < len(a) and curr_b < len(b):
        if a[curr_a] < b[curr_b]:
            auxiliary_arr.append(a[curr_a])
            curr_a += 1
        else:
            auxiliary_arr.append(b[curr_b])
            curr_b += 1
    auxiliary_arr += a[curr_a:]
    auxiliary_arr += b[curr_b:]
    return auxiliary_arr


a = [1, 2, 4, 6, 7]
b = [2, 3, 5, 9, 99]

print(marge_2_sorted_arrays(a, b))


def median_of_2_sorted_array(a, b):
    merged_arr = marge_2_sorted_arrays(a, b)
    if len(merged_arr) % 2 == 0:
        return merged_arr[]
