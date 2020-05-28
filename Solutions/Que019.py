
import sys


def min_cost(min_cost_matrix, houses, colors):
    if not min_cost_matrix:
        return 0

    old_min = 0
    old_min_index = -1
    old_second_min = 0

    for c in range(houses):
        current_min = sys.maxsize
        current_second_min = sys.maxsize
        current_min_index = 0

        for d in range(colors):
            if old_min_index == d:
                min_cost_matrix[c][d] += old_second_min

            else:
                min_cost_matrix[c][d] += old_min

            # update the lowest value
            if current_min > min_cost_matrix[c][d]:
                current_second_min = current_min
                current_min = min_cost_matrix[c][d]
                current_min_index = d

            # update the second minimum value of cost
            elif current_second_min > min_cost_matrix[c][d]:
                current_second_min = min_cost_matrix[c][d]

        old_min = current_min
        old_second_min = current_second_min
        old_min_index = current_min_index

    return min(min_cost_matrix[houses - 1])


min_cost_matrix = \
    [[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6]]
print(min_cost(min_cost_matrix, len(min_cost_matrix), len(min_cost_matrix[0])))
