"""
See Q2-PowerArrangers-tree-TLE.py.
Here we specify that ONLY 1 pattern is missing.
"""
def get_figure_name(pos):
    print(pos + 1, flush=True)  # pos ranged from 1 to 595 (inclusive)
    f_name = input()
    return f_name


def get_sets_with_certain_figure_in_pos(offset, set_pos):
    # given a list of positions (point to the first figure),
    #  find all figure names at "offset" position
    sets_with_certain_figure_in_pos = {
        f_name: list()
        for f_name in 'A B C D E'.split()
    }
    for pos in set_pos:
        f_name = get_figure_name(pos + offset)
        sets_with_certain_figure_in_pos[f_name].append(pos)

    return sets_with_certain_figure_in_pos


def find_remained_pattern():
    pattern = list()
    # num_sets_with_f_name = {  # for n = 3
    #     0: 6,
    #     1: 2,
    #     2: 1,
    #     3: 1
    # }
    num_sets_with_f_name = {
        0: 120,
        1: 24,
        2: 6,
        3: 2,
        4: 1,
        5: 1
    }
    pos_list = [i for i in range(0, 595, 5)]  # 15 or 595, 3 or 5

    # iterate over figure position (from 1 to 5)
    # for each iteration, check which figure name is lesser than other
    # given this figure name, find missing pattern by counting sets at of figure name next position
    for i in range(5):
        sets = get_sets_with_certain_figure_in_pos(i, pos_list)

        # pop included char
        for c in pattern:
            sets.pop(c)

        for f_name, sub_pos_list in sets.items():
            if len(sub_pos_list) != num_sets_with_f_name[i + 1]:
                pattern.append(f_name)
                pos_list = sub_pos_list

    # return result
    print(''.join(pattern), flush=True)
    verdict = input()
    if verdict == 'N':
        exit()


if __name__ == '__main__':
    n_case, max_inspection = [int(s) for s in input().split()]
    for case_id in range(n_case):
        find_remained_pattern()
