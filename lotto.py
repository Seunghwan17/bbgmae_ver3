import random


def pick_lotto_numbers(start=1, end=45, count=6):
    return sorted(random.sample(range(start, end + 1), count))


if __name__ == '__main__':
    print(pick_lotto_numbers())
