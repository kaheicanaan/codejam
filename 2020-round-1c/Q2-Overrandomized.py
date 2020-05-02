from pprint import pprint
from collections import defaultdict


def test_set_3():
    U = int(input())
    mapping = defaultdict(int)
    for _ in range(10 ** 4):
        m, r = input().split(' ')

        for c in r:
            if c not in mapping:
                mapping[c] = 0

        c = r[0]
        mapping[c] += 1

    secret_string = sorted(mapping.items(), key=lambda t: t[1], reverse=True)
    secret_string = [k for k, v in secret_string]
    return secret_string[-1] + ''.join(secret_string[:-1])


def find_digit_string():
    # init
    U = int(input())
    mapping = dict()

    for _ in range(10 ** 4):
        m, r = input().split(' ')

        for c in r:
            if c not in mapping:
                mapping[c] = {i for i in range(10)}

        if m == '-1':  # Q = -1
            continue

        if len(m) != len(r):
            continue
        else:
            # using first digit
            c = r[0]

            mapping[c] &= {i for i in range(1, int(m[0]) + 1)}

    secret_string = ['-' for _ in range(10)]
    digit_seen = set()

    for _ in range(10):
        for k, digit_set in mapping.items():
            digit_unseen = {i for i in digit_set if i not in digit_seen}
            if len(digit_unseen) == 1:
                i = digit_unseen.pop()
                secret_string[i] = k
                digit_seen.add(i)

    return ''.join(secret_string)


if __name__ == '__main__':
    t = int(input())
    for case_id in range(1, t + 1):
        string = test_set_3()
        print('Case #{}: {}'.format(case_id, string))
