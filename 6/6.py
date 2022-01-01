from typing import Optional, Tuple

FILENAME = 'input.txt'
DAYS = 0

with open(FILENAME, 'r') as fo:
    initial = [int(x) for x in fo.readline().split(',')]

def increment_lanternfish(old_value) -> Tuple[int, Optional[int]]:
    new_value = old_value - 1
    if new_value < 0 :
        return 6, 8
    return new_value, None

status = initial.copy()
for i in range(DAYS):
    day = i+1
    news = []
    for f, fish in enumerate(status):
        fish_inc, new = increment_lanternfish(fish)
        status[f] = fish_inc
        if new is not None:
            news.append(new)
    status = status + news
    print(f'After {day:2} days: {len(status)} fishes')

# Faster version
MORE_DAYS = 256
fishes_with_age = [0 for _ in range(9)]
for f in initial:
    fishes_with_age[f] += 1


for i in range(MORE_DAYS):
    day = i+1
    new_fishes = fishes_with_age[0]
    for i in range(len(fishes_with_age)-1):
        fishes_with_age[i] = fishes_with_age[i+1]
    fishes_with_age[6] += new_fishes
    fishes_with_age[8] = new_fishes # replace
    print(f'After {day:2} days: {sum(f for f in fishes_with_age)} fishes')


