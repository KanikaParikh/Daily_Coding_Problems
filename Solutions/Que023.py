
from copy import deepcopy


def add_cache(coordinate, cache):
    new_cache = deepcopy(cache)
    new_cache.add("{}-{}".format(coordinate[0], coordinate[1]))
    return new_cache


def visit(coordinate, cache):
    return "{}-{}".format(coordinate[0], coordinate[1]) in cache


def path(maze, row, col, start, end, cache):
    if start == end:
        return 0
    cache = add_cache(start, cache)

    def visit_neighbour(coordinate):
        if not visit(coordinate, cache) and \
                maze[coordinate[0]][coordinate[1]] != "True":
            length = path(maze, row, col, coordinate, end, cache)
            if length != None:
                path_length.append(length)

    path_length = list()

    if start[0] != 0:
        coordinate = (start[0] - 1, start[1])
        visit_neighbour(coordinate)

    if start[0] != row - 1:
        coordinate = (start[0] + 1, start[1])
        visit_neighbour(coordinate)

    if start[1] != 0:
        coordinate = (start[0], start[1] - 1)
        visit_neighbour(coordinate)

    if start[1] != col - 1:
        coordinate = (start[0], start[1] + 1)
        visit_neighbour(coordinate)

    return min(path_length) + 1 if path_length else None


matrix = [["False", "False", "False", "False"],
          ["True", "True", "True", "False"],
          ["False", "False", "False", "False"],
          ["False", "False", "False", "False"]]

print(path(matrix, len(matrix), len(
    matrix[0]), (0, 0), (0, 0), set()))  # 0
print(path(matrix, len(matrix), len(
    matrix[0]), (1, 0), (0, 0), set()))  # 1
print(path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 0), set()))  # 9
print(path(matrix, len(matrix), len(
    matrix[0]), (2, 0), (3, 3), set()))  # 4
print(path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 3), set()))  # 6
