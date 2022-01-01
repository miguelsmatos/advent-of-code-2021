import numpy as np

FILENAME = 'input.txt'

with open(FILENAME, 'r') as fo:
    positions = [int(x) for x in fo.readline().split(',')]
p = np.array(positions)

av = sum(positions) / len(positions)
print(f'Starting with {len(positions)} positions, average is {av}')

min_cost = sum(positions)
for i in range(min(positions), max(positions)):
    moves = np.abs(p-i)
    cost = np.sum(np.abs(p-i))
    min_cost = min(cost, min_cost)
    print(f'Cost of moving to position {i} -> {cost}')

min_cost = sum(positions)**4 # large enough
for i in range(min(positions), max(positions)):
    moves = np.abs(p-i)
    cost = np.sum(moves*(moves+1)/2).astype(np.int)
    min_cost = min(cost, min_cost)
    print(f'Cost of moving to position {i} -> {cost}')

print(f"Min cost = {min_cost}")

# new cost
# 1 -> 1
# 2 -> 1 + 2 = 3
# 3 -> 1 + 2 + 3 = 6
# 4 -> 1 + 2 + 3 + 4 = 10
# triangular sequence -> n(n+1)/2