# The function gets 2 inputs: arr of numbers and int sum, and return bool = the arr has_two_nums_sums_n

n = 8
arr1 = [1, 2, 3, 6]  # should return True
arr2 = [1, 2, 3, 44]  # should return False


def has_two_nums_sums_n(arr, n):
    sums_dict = {}
    for num in arr:
        if sums_dict.get(n - num):
            return True
        sums_dict[num] = True

    return False


print(has_two_nums_sums_n(arr1, n))
print(has_two_nums_sums_n(arr2, n))
