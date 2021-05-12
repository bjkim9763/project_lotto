import random


def generate_numbers(i):
    numbers = list(range(1, 46))
    return random.sample(numbers, i)


def draw_winning_numbers():
    result = generate_numbers(7)
    return sorted(result[:6]) + result[6:]


def count_matching_numbers(list_1, list_2):
    cnt = 0
    i = 0
    while i < len(list_1):
        if list_1[i] in list_2:
            cnt += 1
            i += 1
        else:
            i += 1
    return cnt


def check(list_1, list_2):
    result = count_matching_numbers(list_1, list_2[:6])
    bonus = count_matching_numbers(list_1, list_2[6:])
    if result == 6:
        return 1000000000
    elif result == 5 and bonus == 1:
        return 50000000
    elif result == 5:
        return 1000000
    elif result == 4:
        return 50000
    elif result == 3:
        return 5000
    else:
        return 0


while True:
    a = generate_numbers(6)
    b = draw_winning_numbers()
    c = count_matching_numbers(a, b)
    d = check(a, b)
    if c == 6:
        print(a)
        print(b)
        print(c)
        print(d)
        break