import random


def pick_lotto_numbers(start=1, end=45, count=6, min_odd=2, max_odd=4):
    # 홀짝 비율이 3:3, 4:2, 2:4 인 조합만 허용
    while True:
        numbers = sorted(random.sample(range(start, end + 1), count))
        odd = sum(n % 2 for n in numbers)
        if min_odd <= odd <= max_odd:
            return numbers


if __name__ == '__main__':
    print(pick_lotto_numbers())
