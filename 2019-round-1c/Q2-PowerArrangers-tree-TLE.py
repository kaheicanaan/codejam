"""
Test set 1 is simple.
We look at 4 of the figures of a set will determine the remained one.
So looking at (595 / 5) * 4 - 1 = 475 (which is F) determines all other figures.

This method can find ALL missing permutations. (Too generic that takes too much time?)
"""
global max_inspection
global prefix_tree


class Node:
    def __init__(self, c):
        self.c = c
        self.parent = None
        self.children = dict()
        self.size = 0


def init_patterns():
    global prefix_tree

    def create_child(node, remained_char):
        if len(remained_char) == 1:
            node.size = 1
            return node

        node.children = {
            c: create_child(Node(c), remained_char.replace(c, ''))
            for c in remained_char
        }
        # for c in remained_char:
        #     child = Node(c)
        #     child.parent = node
        #     node.children.update({c: child})
        #     create_child(child, remained_char.replace(c, ''))

        node.size = sum([child.size for child in node.children.values()])
        return node

    prefix_tree = Node('H')
    create_child(prefix_tree, 'ABCDE')  # 'ABC' or 'ABCDE'


def print_tree():
    global prefix_tree

    def print_node(node, space):
        print(space, node.c, node.size)
        for child_name, child in node.children.items():
            print_node(child, space + '--')

    print('=' * 50)
    print_node(prefix_tree, '')
    print('=' * 50)


def get_figure_name(pos):
    print(pos + 1, flush=True)  # pos ranged from 1 to 595 (inclusive)
    f_name = input()
    return f_name


# def reduce_size_by_one(node):
#     node.size -= 1
#     if node.parent:
#         reduce_size_by_one(node.parent)


def discover_pattern(node, pos):
    node.size -= 1
    f_name = get_figure_name(pos)
    child = node.children[f_name]
    if child.size == 1:  # uniquely defined the set (with prior knowledge of sets seen)
        # pop out this child
        node.children.pop(f_name)
    else:  # further inspection of f_name is needed
        discover_pattern(child, pos + 1)


def get_final_pattern(pattern):
    all_f_names = 'A B C D E'.split(' ')  # 'A B C' or 'A B C D E'
    for c in pattern:
        all_f_names.remove(c)

    final_pattern = pattern + all_f_names
    return final_pattern


def find_remained_pattern():
    global prefix_tree
    # init tree
    init_patterns()
    # print_tree()

    # remove patterns by visiting them
    for s_id in range(119):  # 5, 23 or 119
        pos = s_id * 5  # 3, 4 ot 5
        discover_pattern(prefix_tree, pos)
        # print_tree()

    # now the prefix_tree should contain only 1 path
    remained_set = list()
    node = prefix_tree
    while True:
        if len(node.children) == 0:
            break
        for child_name, child in node.children.items():
            remained_set.append(child_name)
            node = child

    # return result
    final_pattern = get_final_pattern(remained_set)
    print(''.join(final_pattern), flush=True)
    verdict = input()
    if verdict == 'N':
        exit()


if __name__ == '__main__':
    n_case, max_inspection = [int(s) for s in input().split()]
    for case_id in range(n_case):
        find_remained_pattern()
