from collections import defaultdict
import numpy as np
from pprint import pprint


def is_valid_destination(ori_cell, dest_cell):
    ori_r, ori_c = ori_cell
    dest_r, dest_c = dest_cell
    if ori_r == dest_r:
        return False
    elif ori_c == dest_c:
        return False
    elif (ori_r - ori_c) == (dest_r - dest_c):
        return False
    elif (ori_r + ori_c) == (dest_r + dest_c):
        return False
    else:
        return True


def is_visited(state, cell, dim):
    i, j = cell
    r, c = dim
    cell_bit_mask = 1 << (i * c + j)
    return state & cell_bit_mask


def get_state(state):
    # list of int -> bit mask
    return int(''.join(map(lambda i: str(i), state)), 2)


def get_state_with_new_cell(ori_state, dest_cell, dim):
    i, j = dest_cell
    r, c = dim
    dest_cell_bit_mask = 1 << (i * c + j)
    return ori_state | dest_cell_bit_mask


def get_state_without_cell(ori_state, last_cell, dim):
    i, j = last_cell
    r, c = dim
    last_cell_bit_mask = 1 << (i * c + j)
    return ori_state ^ last_cell_bit_mask


def get_path(paths, dim):
    r, c = dim
    max_steps = r * c
    path = list()
    # using the first cell seen to compute the path
    current_state = get_state([1 for _ in range(max_steps)])
    current_cell = paths[max_steps][current_state]
    path.append(current_cell)
    for s in range(1, max_steps):
        step = max_steps - s
        # choose a cell such that the transition is valid
        current_state = get_state_without_cell(current_state, current_cell, dim)
        current_cell = paths[step][current_state]
        path.append(current_cell)

    path.reverse()
    return path


def path_search(r, c, starting_cell=(0, 0)):
    # init
    dim = (r, c)
    max_steps = r * c
    # computed_path = [defaultdict(list) for _ in range(max_steps + 1)]  # state -> previous state, last pos
    computed_path = [dict() for _ in range(max_steps + 1)]
    first_state = [
        [0 for col in range(c)]
        for row in range(r)
    ]
    first_state = 1 << (starting_cell[0] * c + starting_cell[1])
    # at first, we use 1 step to go to cell (0, 0)
    computed_path[1][first_state] = starting_cell

    # walk through the matrix
    for step_used in range(1, max_steps):
        # get all current states that reachable by exactly n step
        for current_state, current_cell in computed_path[step_used].items():
            # find possible cells and try to walk into that cell
            for i in range(r):
                for j in range(c):
                    if is_valid_destination(current_cell, (i, j)) and (not is_visited(current_state, (i, j), dim)):
                        new_state = get_state_with_new_cell(current_state, (i, j), dim)
                        computed_path[step_used + 1][new_state] = (i, j)

    # pprint(computed_path)
    # get possible path
    final_state = get_state([1 for _ in range(max_steps)])
    if final_state in computed_path[max_steps]:
        return True, get_path(computed_path, dim)
    else:
        return False, None


stdin_1 = """
2
2 2
2 5

"""


if __name__ == '__main__':
    n_test = int(input())
    for test_id in range(n_test):
        dim_r, dim_c = input().split(' ')
        is_possible, path = path_search(int(dim_r), int(dim_c))
        if is_possible:
            print('Case #{0}: POSSIBLE'.format(test_id + 1))
            for cell_i, cell_j in path:
                print(cell_i + 1, cell_j + 1)
        else:
            print('Case #{0}: IMPOSSIBLE'.format(test_id + 1))
