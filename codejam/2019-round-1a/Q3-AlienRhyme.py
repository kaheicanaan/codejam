global n_words
global words
global max_char
global prefix_tree


def read_words():
    global n_words
    global words
    global max_char

    max_char = 0
    for _ in range(n_words):
        word = input()[::-1]
        words.append(word)
        max_char = max(max_char, len(word))


class Node:
    def __init__(self, char):
        self.char = char
        self.next = list()
        self.count = 0


def add_word_to_tree(current_node, word):
    if len(word) == 0:
        current_node.count = 1
        return

    # find proper entry
    c = word[:1]
    match_node = None
    for node in current_node.next:
        if node.char == c:
            match_node = node

    if not match_node:
        match_node = Node(c)
        current_node.next.append(match_node)

    # add word recursively
    add_word_to_tree(match_node, word[1:])
    return


def count_all_rhymes():
    global n_words
    global words
    global max_char
    global prefix_tree

    for word in words:
        add_word_to_tree(prefix_tree, word)


def modify_count_of_children(node):
    # adjust count
    sum_of_children_count = 0
    for child_node in node.next:
        # go to leaves
        modify_count_of_children(child_node)
        sum_of_children_count += child_node.count

    # 2 unpaired word will pair up using prefix start from this node
    node.count = (node.count + sum_of_children_count)
    if node.count >= 2:
        if not node.char == '':  # except for head node (prefix = '')
            node.count -= 2


def print_count():
    global prefix_tree

    def dfs(node):
        print(node.char, node.count)
        for n in node.next:
            dfs(n)

    dfs(prefix_tree)


def maximize_rhyme(n):
    global n_words
    global words
    global max_char
    global prefix_tree

    # init
    n_words = n
    words = list()
    max_char = 0
    read_words()

    prefix_tree = Node('')  # head
    count_all_rhymes()

    # count number of unmatched words
    modify_count_of_children(prefix_tree)
    return len(words) - prefix_tree.count



stdin_1 = """
CODEJAM
JAM
HAM
NALAM
HUM
NOLOM

"""

stdin_2 = """
4
2
TARPOL
PROL
3
TARPOR
PROL
TARPRO
6
CODEJAM
JAM
HAM
NALAM
HUM
NOLOM
4
PI
HI
WI
FI

"""


if __name__ == '__main__':
    # print(maximize_rhyme(6))
    # exit()
    n_case = int(input())
    for case_id in range(1, n_case + 1):
        number_of_words = int(input())
        max_words_with_rhyme = maximize_rhyme(number_of_words)
        print('Case #{0}: {1}'.format(case_id, max_words_with_rhyme))