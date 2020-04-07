"""
To pass test set 1 is simple. We have sufficient number of days and limited number of gophers.
Just try all blades number (All 18 windmill share the same blade numbers).
Use reminder to determine which number is the most probable.
"""

global possible_numbers


def find_number_of_gophers(n, m):
    global possible_numbers
    possible_numbers = [0 for _ in range(m + 1)]

    # prime_numbers = [2, 3, 5, 7, 9, 11, 13, 17]
    prime_numbers = [i for i in range(2, 19)]
    for day in range(8):
        # print number of blades in each windmill
        prime = prime_numbers[day]
        number_of_blades = [str(prime) for _ in range(18)]
        print(' '.join(number_of_blades))

        # receive movements from judge
        blade_movement = input().split(' ')
        blade_movement = [int(i) for i in blade_movement]
        residue = sum(blade_movement) % prime
        for i in range(0, m + 1, prime):
            if i + residue > m:
                break
            possible_numbers[i + residue] += 1
        print(possible_numbers)

    # determine the possible number of gophers
    largest_number_seen = 0
    number_of_gophers = 0
    for i in range(m + 1):
        temp_count = possible_numbers[i]
        if temp_count > largest_number_seen:
            largest_number_seen = temp_count
            number_of_gophers = i
    print(number_of_gophers)
    verdict = input()
    if verdict == '-1':
        exit()


if __name__ == '__main__':
    t, n, m = input().split()
    t, n, m = int(t), int(n), int(m)
    for _ in range(t):
        find_number_of_gophers(n, m)
