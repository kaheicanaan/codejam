def is_photo_taken(x, y, c):
    return abs(x) + abs(y) <= c


def shortest_path():
    # init
    X, Y, path = input().split(' ')
    X, Y = int(X), int(Y)

    count = 0
    for direction in path:
        if direction == 'N':
            Y += 1
        elif direction == 'E':
            X += 1
        elif direction == 'S':
            Y -= 1
        elif direction == 'W':
            X -= 1
        else:
            raise ValueError()

        count += 1
        if is_photo_taken(X, Y, count):
            return count

    return -1


"""
5
4 4 SSSS
3 0 SNSS
2 10 NSNNSN
0 1 S
2 7 SSSSSSSS

2
3 2 SSSW
4 0 NESW

"""


if __name__ == '__main__':
    t = int(input())
    for case_id in range(1, t + 1):
        steps = shortest_path()
        if steps == -1:
            steps = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(case_id, steps))
