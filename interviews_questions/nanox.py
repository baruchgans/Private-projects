# First question - design. design a system like facebook where each one has list of friends,
# and he can ask another person for friendship.
# the second one was the next question: find_max_occupancy


from collections import OrderedDict


def find_max_occupancy(incoming, outgoing):
    res_dict = {}
    for i in incoming:
        res_dict[i] = res_dict.get(i, 0) + 1
    for i in outgoing:
        res_dict[i] = res_dict.get(i, 0) - 1

    order_res = OrderedDict(sorted(res_dict.items()))
    max_occupancy = 0
    for occupancy in order_res.values():
        max_occupancy = max(max_occupancy, max_occupancy + occupancy)

    return max_occupancy


def find_max_occupancy_v2(incoming, outgoing):
    hours = [0] * 24
    for i in incoming:
        hours[i] += 1
    for o in outgoing:
        hours[o] -= 1
    max_occupancy = 0
    for count in hours:
        max_occupancy = max(max_occupancy, max_occupancy + count)
    return max_occupancy


a = [0, 1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10, 11]
print(find_max_occupancy(a, b))
print(find_max_occupancy_v2(a, b))
