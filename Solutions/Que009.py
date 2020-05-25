import sys

def get_non_adj_sum(array):

    previous = 0
    largest = 0

    for amt in array:
        #print("amt: {}; previous: {}; largest: {}".format(amt, previous, largest))
        previous, largest = largest, max(largest, previous + amt)
        #print("new_previous: {}; new_largest: {}".format(previous, largest))
    return largest

print(get_non_adj_sum([2, 4, 6, 8]))
print(get_non_adj_sum([5, 1, 1, 5]))
