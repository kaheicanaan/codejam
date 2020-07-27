import functools


def check_strings(sub_words, is_prefix=True):
    # for each pattern, find longest string (other string must be a prefix/suffix of longest string)
    longest_string = ''
    for sub_word in sub_words:
        if len(longest_string) < len(sub_word):
            longest_string = sub_word

    # check other sub words are prefix/suffix of longest sub word
    checker = longest_string.startswith if is_prefix else longest_string.endswith
    for sub_word in sub_words:
        if checker(sub_word):
            pass
        else:
            return False, ''

    return True, longest_string


def find_name():
    # init
    n_words = int(input())
    words = [input().split('*') for _ in range(n_words)]

    result = list()
    # first sub words
    is_possible, matched_substring = check_strings([word[0] for word in words])
    if is_possible:
        result.append(matched_substring)
    else:
        return '*'

    # last sub words
    is_possible, matched_substring = check_strings([word[-1] for word in words], is_prefix=False)
    if is_possible:
        result.append(matched_substring)
    else:
        return '*'

    # get middle parts
    for word in words:
        word.pop(0)
        word.pop(-1)
    # join all middle part
    sub_strings = ''.join([''.join(word) for word in words])

    # total result
    result.insert(1, sub_strings)
    return ''.join(result)



stdin_1 = """
2
5
*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S
2
*XZ
*XYZ

1
4
H*O
HELLO*
*HELLO
HE*

1
2
A*C*E
*B*D*

1
2
A*E
*B*D*

"""


if __name__ == '__main__':
    n_case = int(input())
    for case_id in range(1, n_case + 1):
        name = find_name()
        print('Case #{0}: {1}'.format(case_id, name))
