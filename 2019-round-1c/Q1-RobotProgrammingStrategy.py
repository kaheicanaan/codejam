"""
C_i is at most 5 (or 500), number of moves to determine winner is at most C_i * (C_i - 1)
"""
import math
from pprint import pprint

global robots


class Robot:
    def __init__(self, moves):
        self.moves = moves
        self.is_eliminated = False

    def __repr__(self):
        return self.moves

    def action(self, move_id):
        move_id = move_id % len(self.moves)
        return self.moves[move_id]


def get_best_move(other_robots_action):
    # return: is_ended, best_move, eliminated_move
    if other_robots_action == {'R'}:
        return True, 'P', 'R'
    elif other_robots_action == {'P'}:
        return True, 'S', 'P'
    elif other_robots_action == {'S'}:
        return True, 'R', 'S'
    elif other_robots_action == {'R', 'P'}:
        return False, 'P', 'R'
    elif other_robots_action == {'R', 'S'}:
        return False, 'R', 'S'
    elif other_robots_action == {'S', 'P'}:
        return False, 'S', 'P'
    elif other_robots_action == {'R', 'P', 'S'}:
        return True, '', ''  # ended due to no solution


def determine_winning_strategy(a):
    global robots

    # init
    robots = list()
    k = int(math.log2(a + 1))
    for robot_id in range(a):
        robots.append(Robot(input()))

    max_number_of_moves = 256
    allowed_moves = list()
    for move_id in range(max_number_of_moves):
        # print('current_robots:', [robot for robot in robots if not robot.is_eliminated])
        # determine which action is the best
        other_robots_action = set([robot.action(move_id) for robot in robots if not robot.is_eliminated])
        is_ended, best_move, eliminated_move = get_best_move(other_robots_action)

        # depending whether the game has been ended in this move
        if is_ended:
            # if there is no possible moves, return "IMPOSSIBLE"
            if best_move == '':
                return 'IMPOSSIBLE'
            else:
                allowed_moves.append(best_move)
                return ''.join(allowed_moves)
        else:
            allowed_moves.append(best_move)
            # eliminate remained robots
            for robot in robots:
                if robot.action(move_id) == eliminated_move:
                    # print('eliminated_robots:', robot)
                    robot.is_eliminated = True

    # cannot finish within maximum number of moves => googol moves reached
    return 'IMPOSSIBLE'


stdin_1 = """
3
1
RS
3
R
P
S
7
RS
RS
RS
RS
RS
RS
RS

"""

stdin_2 = """
1
3
RS
SR
RPS

"""

stdin_3 = """
1
3
RS
SR
RR

"""


if __name__ == '__main__':
    n_case = int(input())
    for case_id in range(1, n_case + 1):
        number_of_players = int(input())
        sequence = determine_winning_strategy(number_of_players)
        print('Case #{0}: {1}'.format(case_id, sequence))
