stdin_1 = """
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

"""

# CJJC
stdin_2 = """
1
4
1 3
8 10
2 7
5 9

"""


class Parent:
    def __init__(self, name):
        self.name = name
        self.schedules = list()

    def add_schedule(self, schedule):
        self.schedules.append(schedule)
        schedule.assigned_to = self.name

    def is_available(self, schedule):
        # make sure input schedule does not collide with any assigned schedules
        is_collided = any([
            self._is_two_schedules_collided(ori_schedule, schedule)
            for ori_schedule in self.schedules
        ])
        # print([ori_schedule.scheduled_time for ori_schedule in self.schedules], schedule.scheduled_time, is_collided)
        return not is_collided

    @staticmethod
    def _is_two_schedules_collided(schedule_1, schedule_2):
        ori_start, ori_end = schedule_1.scheduled_time
        new_start, new_end = schedule_2.scheduled_time

        if new_start < ori_start:
            if new_end <= ori_start:
                return False
            else:
                return True
        elif ori_start <= new_start < ori_end:
            return True
        else:  # ori_end <= new_start
            return False


class Schedule:
    def __init__(self, start, end):
        self.scheduled_time = (start, end)
        self.assigned_to = None


def get_priority(schedules):
    pos_and_attr = list(enumerate([schedule.scheduled_time[1] for schedule in schedules]))
    pos_and_attr = sorted(pos_and_attr, key=lambda tup: tup[1], reverse=True)
    return [pos for pos, interval in pos_and_attr]


def assign_schedules():
    # init parent
    parents = [Parent('C'), Parent('J')]
    n_schedule = int(input())
    schedules = list()

    # get schedules
    for _ in range(n_schedule):
        schedule = input().split()
        start, end = int(schedule[0]), int(schedule[1])
        schedules.append(Schedule(start, end))

    # check availability and assign schedule
    for schedule_id in get_priority(schedules):
        schedule = schedules[schedule_id]
    # for schedule in schedules:  # todo: assign schedule according to priority
        # print(schedule.scheduled_time)
        cameron = parents[0]
        jamie = parents[1]
        if cameron.is_available(schedule):
            cameron.add_schedule(schedule)
            # print(f'job {schedule.scheduled_time} is assigned to Cameron')
        elif jamie.is_available(schedule):
            jamie.add_schedule(schedule)
            # print(f'job {schedule.scheduled_time} is assigned to Jamie')
        else:
            # print(f'job {schedule.scheduled_time} is impossible to be assigned')
            return 'IMPOSSIBLE'

    # return all assigned schedules with parent names
    names = [schedule.assigned_to for schedule in schedules]
    return ''.join(names)


def test_collision():
    schedule_pairs = [
        [Schedule(100, 200), Schedule(90, 95)],  # False
        [Schedule(100, 200), Schedule(99, 100)],  # False
        [Schedule(100, 200), Schedule(99, 101)],  # True

        [Schedule(100, 200), Schedule(100, 101)],  # True
        [Schedule(100, 200), Schedule(100, 200)],  # True
        [Schedule(100, 200), Schedule(100, 201)],  # True

        [Schedule(100, 200), Schedule(150, 160)],  # True
        [Schedule(100, 200), Schedule(150, 200)],  # True
        [Schedule(100, 200), Schedule(150, 201)],  # True

        [Schedule(100, 200), Schedule(200, 201)],  # False

        [Schedule(100, 200), Schedule(201, 210)],  # False
    ]
    for pair in schedule_pairs:
        print(pair[0].scheduled_time, pair[1].scheduled_time, Parent._is_two_schedules_collided(*pair))


if __name__ == '__main__':
    n_test = int(input())
    for test_id in range(n_test):
        output = assign_schedules()
        print('Case #{0}: {1}'.format(test_id + 1, output), flush=True)
