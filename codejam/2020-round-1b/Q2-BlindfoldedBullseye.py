global case_id
global a, b
global MAX_INT, MIN_INT
import math


class UnexpectedlyGotCorrectAnswer(BaseException):
    pass


def test_pos(i, j):
    print(i, j)
    verdict = input()
    if verdict == 'CENTER':
        raise UnexpectedlyGotCorrectAnswer()
    else:
        return verdict


def get_starting_points():
    global a, b, MAX_INT, MIN_INT
    for t_i in range(MIN_INT, MAX_INT, a):
        for t_j in range(MIN_INT, MAX_INT, a):
            verdict = test_pos(t_i, t_j)
            if verdict == 'HIT':
                return t_i, t_j
            elif verdict == 'CENTER':
                raise UnexpectedlyGotCorrectAnswer()


def x_binary_search(ranged_t_i, t_j, hit='r'):
    i_1, i_2 = ranged_t_i

    if i_2 - i_1 == 0:
        return i_1
    elif i_2 - i_1 == 1:
        verdict = test_pos(i_1, t_j)
        if verdict == 'HIT':
            return i_1
        else:
            return i_2

    test_t_i = math.floor((i_1 + i_2) / 2)
    verdict = test_pos(test_t_i, t_j)
    if verdict == 'HIT':
        if hit == 'r':
            return x_binary_search((i_1, test_t_i), t_j, hit='r')
        else:
            return x_binary_search((test_t_i, i_2), t_j, hit='l')
    elif verdict == 'MISS':
        if hit == 'r':
            return x_binary_search((test_t_i, i_2), t_j, hit='r')
        else:
            return x_binary_search((i_1, test_t_i), t_j, hit='l')


def y_binary_search(ranged_t_j, t_i, hit='u'):
    j_1, j_2 = ranged_t_j

    if j_2 - j_1 == 0:
        return j_1
    elif j_2 - j_1 == 1:
        verdict = test_pos(t_i, j_1)
        if verdict == 'HIT':
            return j_1
        else:
            return j_2

    test_t_j = (j_1 + j_2) // 2
    verdict = test_pos(t_i, test_t_j)
    if verdict == 'HIT':
        if hit == 'u':
            return y_binary_search((j_1, test_t_j), t_i, hit='u')
        else:
            return y_binary_search((test_t_j, j_2), t_i, hit='d')
    elif verdict == 'MISS':
        if hit == 'u':
            return y_binary_search((test_t_j, j_2), t_i, hit='u')
        else:
            return y_binary_search((j_1, test_t_j), t_i, hit='d')


def find_bulls_eye():
    global case_id
    global a, b, MAX_INT, MIN_INT
    # randomly shoot until a dart hit the board
    searching_points = get_starting_points()
    s_i, s_j = searching_points
    x_min = x_binary_search((MIN_INT, s_i), s_j, hit='r')
    x_max = x_binary_search((s_i, MAX_INT), s_j, hit='l')
    y_min = y_binary_search((MIN_INT, s_j), s_i, hit='u')
    y_max = y_binary_search((s_j, MAX_INT), s_i, hit='d')

    target_x = (x_min + x_max) // 2
    target_y = (y_min + y_max) // 2
    for near_target_x in range(target_x - 2, target_x + 3):
        for near_target_y in range(target_y - 2, target_y + 3):
            verdict = test_pos(near_target_x, near_target_y)
            if verdict == 'CENTER':
                return
    print(case_id, 'target:', verdict, target_x, target_y)
    exit()


"""
1 500000000 1000000000

1 999999950 999999950

"""


if __name__ == '__main__':
    global case_id, a, b, MAX_INT, MIN_INT
    MAX_INT = 1000000000
    MIN_INT = -1000000000

    t, a, b = [int(s) for s in input().split(' ')]
    for case_id in range(1, t + 1):
        try:
            find_bulls_eye()
        except UnexpectedlyGotCorrectAnswer:
            pass
