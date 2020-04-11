import math
import random

global visited
global nCr_cache
global path

def nCr(pos):
    global nCr_cache

    if pos in nCr_cache:
        return nCr_cache[pos]
    else:
        n, r = pos[0] - 1, pos[1] - 1
        f = math.factorial
        value = int(f(n) / f(r) / f(n-r))
        nCr_cache.update({pos: value})
        return value


def get_possible_pos(pos):
    global visited
    n, r = pos
    possible_pos = [
        (n - 1, r - 1),
        (n - 1, r),
        (n, r - 1),
        (n, r + 1),
        (n + 1, r),
        (n + 1, r + 1)
    ]

    for pos in possible_pos[:]:
        pos_n, pos_r = pos
        if (pos_n < 1) or (pos_r < 1) or (pos_r > pos_n):
            possible_pos.remove(pos)

    possible_pos = [pos for pos in possible_pos if pos not in visited]
    possible_pos = sorted(possible_pos, key=lambda pos: nCr(pos), reverse=True)
    return possible_pos


class PathFoundSignal(BaseException):
    pass


def DFS(pos, sum_, TTL):
    global visited
    global path

    if TTL == 0:
        return

    if sum_ == 0:
        raise PathFoundSignal

    possible_pos = get_possible_pos(pos)
    for pos in possible_pos:
        if nCr(pos) <= sum_:
            visited.add(pos)
            path.append(pos)
            DFS(pos, sum_ - nCr(pos), TTL - 1)
            visited.remove(pos)
            path.pop()


def find_path(sum_):
    global visited
    global path
    pos = (1, 1)
    visited = set()
    visited.add(pos)
    path = [pos]

    try:
        DFS(pos, sum_ - 1, 499)
    except PathFoundSignal:
        _sum = 0
        for pos in path:
            print(*pos)
            _sum += nCr(pos)
        print(len(path), _sum)



stdin_1 = """
3
1
4
19

"""


if __name__ == '__main__':
    global nCr_cache
    nCr_cache = dict()

    n_case = int(input())
    for case_id in range(1, n_case + 1):
        print('Case #{0}:'.format(case_id))
        _sum = int(input())
        find_path(_sum)
