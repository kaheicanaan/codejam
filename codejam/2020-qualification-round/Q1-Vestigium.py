stdin_1 = """
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

"""


def check_latin_square():
    # read inputs
    dim = int(input())
    matrix = list()
    for row_id in range(dim):
        row = input().split(' ')
        row = [int(v) for v in row]
        matrix.append(row)

    # check duplicates in row
    r = 0
    for i in range(dim):
        value_set = set()
        for j in range(dim):
            value_set.add(matrix[i][j])
        if len(value_set) < dim:
            r += 1
    # check duplicates in col
    c = 0
    for j in range(dim):
        value_set = set()
        for i in range(dim):
            value_set.add(matrix[i][j])
        if len(value_set) < dim:
            c += 1

    # output
    trace = 0
    for i in range(dim):
        trace += matrix[i][i]
    return trace, r, c


if __name__ == '__main__':
    n_test = int(input())
    for test_id in range(n_test):
        trace, r, c = check_latin_square()
        print('Case #{0}: {1} {2} {3}'.format(test_id + 1, trace, r, c))
