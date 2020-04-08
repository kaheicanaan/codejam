import collections
from pprint import pprint


global n_words
global words
global max_char
global common_prefix_words
global included_words
global included_prefixes


def read_words():
    global n_words
    global words
    global max_char

    max_char = 0
    for _ in range(n_words):
        word = input()[::-1]
        words.append(word)
        max_char = max(max_char, len(word))


def count_all_rhymes():
    global n_words
    global words
    global max_char
    global common_prefix_words

    # count all possible pairs
    for i in range(n_words):
        for j in range(i + 1, n_words):
            word_1 = words[i]
            word_2 = words[j]
            for k in range(1, max_char):
                # be careful the length of words
                if (len(word_1) < k) or (len(word_2) < k):
                    break
                if word_1[:k] == word_2[:k]:
                    common_prefix_words[k][word_1[:k]].append((word_1, word_2))


def maximize_rhyme(n):
    global n_words
    global words
    global max_char
    global common_prefix_words
    global included_words
    global included_prefixes

    # init
    n_words = n
    words = list()
    max_char = 0
    read_words()

    common_prefix_words = [collections.defaultdict(list) for _ in range(max_char + 1)]
    count_all_rhymes()
    # pprint(common_prefix_words)

    # count pairs from longest matched pairs
    included_words = set()
    included_prefixes = set()
    for i in range(max_char, 0, -1):
        # print(i)
        matched_pairs = common_prefix_words[i]
        # pprint(matched_pairs)
        # within this layer, all matched pairs are unique (i.e. words will not appears more than once)
        for prefix, pairs in matched_pairs.items():
            # if this prefix is added, no need to check other pairs
            if prefix in included_prefixes:
                continue

            for word_1, word_2 in pairs:
                # if any one of these words are included in previous layer, ignore this pair
                if (word_1 in included_words) or (word_2 in included_words):
                    pass
                else:
                    included_words.add(word_1)
                    included_words.add(word_2)
                    included_prefixes.add(prefix)
                    break  # also break word pairs loop

    # print(included_words)
    return len(included_words)




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
    n_case = int(input())
    for case_id in range(1, n_case + 1):
        number_of_words = int(input())
        max_words_with_rhyme = maximize_rhyme(number_of_words)
        print('Case #{0}: {1}'.format(case_id, max_words_with_rhyme))
