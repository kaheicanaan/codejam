"""
Key optimization:
1. Graph can be adjusted using O(1) time during elimination process.
2. For node(s) that all its neighbours is not eliminated, will not be eliminated at next loop.
"""


class Node:
    all_nodes = dict()

    def __init__(self, pos, skill):
        self.all_nodes.update({pos: self})
        self.pos = pos
        self.skill = int(skill)
        self.w = None
        self.a = None
        self.s = None
        self.d = None
        self.is_eliminated = False

    def neighbours(self):
        return [self.w, self.a, self.s, self.d]

    def avg_level(self):
        neighbours = [self.w, self.a, self.s, self.d]
        levels = [n.skill for n in neighbours if n]
        l = len(levels)
        if l == 0:
            return 0.0
        else:
            return sum(levels) / l

    def is_less_skillful(self):
        return self.skill < self.avg_level()

    # def __repr__(self):
    #     return f'({self.pos} skill={self.skill}, neighbours={[n.skill for n in self.neighbours() if n]}'


def get_interest_level():
    # init
    Node.all_nodes = dict()
    r, c = [int(_) for _ in input().split(' ')]
    skill_levels = [input().split(' ') for _ in range(r)]

    # create nodes
    for i in range(r):
        for j in range(c):
            Node((i, j), skill_levels[i][j])

    # link nodes
    for i in range(r):
        for j in range(c):
            node = Node.all_nodes[(i, j)]
            if i != 0:
                w_node = Node.all_nodes[(i - 1, j)]
                node.w = w_node
            if j != 0:
                a_node = Node.all_nodes[(i, j - 1)]
                node.a = a_node
            if i != r - 1:
                s_node = Node.all_nodes[(i + 1, j)]
                node.s = s_node
            if j != c - 1:
                d_node = Node.all_nodes[(i, j + 1)]
                node.d = d_node

    nodes = list(Node.all_nodes.values())
    node_to_be_checked = [nodes]

    # calculate interest level
    interest_level = 0
    current_interest_level_sum = sum([node.skill for node in nodes])
    stage = 0
    while True:
        node_to_be_checked.append(list())  # for next loop
        if len(node_to_be_checked[stage]) == 0:
            break

        # add interest level
        interest_level += current_interest_level_sum

        # check if node is eliminated
        nodes_will_be_eliminated = [node for node in node_to_be_checked[stage] if node.is_less_skillful()]
        node_to_be_checked_at_next_stage = dict()

        # now eliminate node(s)
        for node in nodes_will_be_eliminated:
            node.is_eliminated = True
            current_interest_level_sum -= node.skill
            if node.w:
                node.w.s = node.s
                node_to_be_checked_at_next_stage.update({node.w.pos: node.w})
            if node.s:
                node.s.w = node.w
                node_to_be_checked_at_next_stage.update({node.s.pos: node.s})
            if node.a:
                node.a.d = node.d
                node_to_be_checked_at_next_stage.update({node.a.pos: node.a})
            if node.d:
                node.d.a = node.a
                node_to_be_checked_at_next_stage.update({node.d.pos: node.d})

        # eliminate node(s) that are in check list
        # node(s) in check list might be eliminated in previous step
        # if eliminated, no checking is required at next loop
        node_to_be_checked[stage + 1] = [node for node in node_to_be_checked_at_next_stage.values() if not node.is_eliminated]
        stage += 1

    return interest_level



stdin_1 = """
1
4 6
3 1 2 9 7 4
3 6 9 6 3 2
4 7 9 4 2 6
9 7 4 3 6 8

4
1 1
15
3 3
1 1 1
1 2 1
1 1 1
1 3
3 1 2
1 3
1 2 3

"""


if __name__ == '__main__':
    n_case = int(input())
    for case_id in range(1, n_case + 1):
        result = get_interest_level()
        print('Case #{0}: {1}'.format(case_id, result))
