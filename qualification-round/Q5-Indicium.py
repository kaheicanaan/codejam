import numpy as np
from datetime import datetime
import copy


cache = dict()


def get_base_matrix(n):
    random_algebra = np.random.permutation([i + 1 for i in range(n)])
    r = np.concatenate([random_algebra, random_algebra])
    m = [r[_:_ + n] for _ in range(n)]
    m = np.array(m)
    return m


def generate_latin_square():
    # todo: it is for test set 1
    allowed_time = {
        2: 1,
        3: 1,
        4: 2,
        5: 4
    }
    for n in range(2, 6):
        start_time = datetime.now()
        while True:
            m = get_base_matrix(n)
            for _ in range(20):
                axis = np.random.choice(['r', 'c'])
                i = np.random.randint(0, n)
                j = np.random.randint(0, n)
                if axis == 'r':
                    m[[i, j]] = m[[j, i]]
                else:
                    m[:, [i, j]] = m[:, [j, i]]

                t = np.trace(m)
                if (n, t) not in cache:
                    cache.update({(n, t): copy.deepcopy(m)})

            if (datetime.now() - start_time).total_seconds() > allowed_time[n]:
                break

    # prettfy cache result
    print(len(cache))
    sorted_keys = list(sorted(cache.keys(), key=lambda tup: tup[0] * (n ** 2) + tup[1]))
    print(sorted_keys)
    for key in sorted_keys:
        print(key)
        print(cache[key])


def generate_indicium(n, k):
    if (n, k) in cache:
        return True, cache[(n, k)]

    return False, None


stdin_1 = """
6
3 6
2 3
4 6
4 4
5 20
5 9

"""


if __name__ == '__main__':
    n_test = int(input())
    generate_latin_square()
    for test_id in range(n_test):
        n_str, t_str = input().split(' ')
        n, t = int(n_str), int(t_str)
        is_possible, _matrix = generate_indicium(n, t)
        if is_possible:
            print('Case #{0}: POSSIBLE'.format(test_id + 1), flush=True)
            pre_output = [' '.join(map(lambda i: str(i), row)) for row in _matrix]
            output = '\n'.join(pre_output)
            print(output)
        else:
            print('Case #{0}: IMPOSSIBLE'.format(test_id + 1), flush=True)
