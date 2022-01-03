import numpy as np

FILENAME = "input.txt"
REPETITIONS = 5  # Change to 1 for the Part 1

locations = []
with open(FILENAME, "r") as fo:
    for line in fo:
        locations.append([int(x) for x in line if x and x.isdigit()])
weights = np.array(locations)

for i in range(2):
    extra = weights.copy()
    for r in range(REPETITIONS - 1):
        extra += 1
        extra[extra == 10] = 1
        if not i:
            weights = np.hstack((weights, extra))
        else:
            weights = np.vstack((weights, extra))

large_value = np.max(weights) * 2 * np.sum(weights.size)  # If all had the max weight
distances = np.ones_like(weights, dtype=int) * large_value
visited = np.zeros_like(weights, dtype=bool)
distances[0, 0] = 0

current = (0, 0)
shape = weights.shape
destination = (shape[0] - 1, shape[1] - 1)

def neighbors(i, j):
    if i > 0:
        yield (i - 1, j)
    if j > 0:
        yield (i, j - 1)
    if i < shape[0] - 1:
        yield (i + 1, j)
    if j < shape[1] - 1:
        yield (i, j + 1)


while not visited[destination]:
    if not visited[current]:
        for n in neighbors(*current):
            if distances[current] + weights[n] < distances[n]:
                distances[n] = distances[current] + weights[n]
        visited[current] = True
    min_d = np.min(distances + visited * large_value)
    min_ijs = np.where(~visited * (distances == min_d))
    current = (min_ijs[0][-1], min_ijs[1][-1])
    if current == destination:
        break
    print(np.sum(visited) / visited.size)

print(f"The minimum cost to reach {destination} is {distances[destination]}")
