import numpy as np
import random
import copy


global case_id
global dim
global nodes
global path
global is_visited


class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.edges = list()

    def __repr__(self):
        return '({0}, {1})'.format(self.i, self.j)


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


def init_nodes():
    global dim
    global nodes
    r, c = dim

    # init node
    for i in range(r):
        for j in range(c):
            node = Node(i, j)
            nodes.update({(i, j): node})

    # add edges to node
    for i in range(r):
        for j in range(c):
            for _i in range(r):
                for _j in range(c):
                    if is_valid_destination((i, j), (_i, _j)):
                        node_1 = nodes[(i, j)]
                        node_2 = nodes[(_i, _j)]
                        node_1.edges.append(node_2)
                        node_2.edges.append(node_1)

    # randomize edges
    for d, node in nodes.items():
        random.shuffle(node.edges)
    # print(nodes)
    # print(nodes[(0, 0)].edges)
    return nodes


class ValidPathFoundException(Exception):
    pass


def DFS(current_node, max_steps):
    global path
    global is_visited

    if max_steps == 0:  # all cell are visited
        raise ValidPathFoundException

    # find non visited node and add it to path
    for node in current_node.edges:
        if is_visited[node.i][node.j]:
            continue
        else:
            path.append(node)
            is_visited[node.i][node.j] = True
            DFS(node, max_steps - 1)

    # no more node to visit and path is still incomplete
    path.pop()
    is_visited[current_node.i][current_node.j] = False


def path_search(r, c):
    global case_id
    global dim
    global nodes
    global path
    global is_visited
    dim = (r, c)
    nodes = dict()
    path = list()
    is_visited = [[False for j in range(c)] for i in range(r)]

    # init graph
    nodes = init_nodes()
    path.append(nodes[(0, 0)])
    is_visited[0][0] = True

    # walk through matrix
    is_possible = False
    try:
        DFS(nodes[(0, 0)], r * c - 1)
    except ValidPathFoundException:
        is_possible = True

    if is_possible:
        print('Case #{0}: POSSIBLE'.format(case_id))
        for node in path:
            print(node.i + 1, node.j + 1)
    else:
        print('Case #{0}: IMPOSSIBLE'.format(case_id))


if __name__ == '__main__':
    global case_id

    n_test = int(input())
    for _id in range(n_test):
        case_id = _id + 1
        dim_r, dim_c = input().split(' ')
        dim_r = int(dim_r)
        dim_c = int(dim_c)
        path_search(dim_r, dim_c)
