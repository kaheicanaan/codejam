stdin1 = """
4
0000
101
111000
1

"""

stdin2 = """
4
021
312
4
221

"""


num_to_parenthesis_mapping = {
    '0': '0',
    '1': '(1)',
    '2': '((2))',
    '3': '(((3)))',
    '4': '((((4))))',
    '5': '(((((5)))))',
    '6': '((((((6))))))',
    '7': '(((((((7)))))))',
    '8': '((((((((8))))))))',
    '9': '(((((((((9)))))))))',
}


def convert_string(input_str):
    output_arr = [num_to_parenthesis_mapping[n] for n in input_str]
    output = ''.join(output_arr)

    # drop every pair of ")("
    for _ in range(9):
        output = output.replace(')(', '')

    # output
    return output


if __name__ == '__main__':
    n_test = int(input())
    for test_id in range(n_test):
        input_str = input()
        output = convert_string(input_str)
        print('Case #{0}: {1}'.format(test_id + 1, output))
