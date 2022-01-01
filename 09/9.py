from typing import Set


FILENAME = "input.txt"

with open(FILENAME, "r") as fo:
    heightmap = []
    for line in fo:
        heightmap.append([int(d) for d in line if d.isdigit()])

low_point_values = []
low_points = []

size_x = len(heightmap[0])
size_y = len(heightmap)

for j in range(size_x):
    for i in range(size_y):
        this_val = heightmap[i][j]
        # left
        if i > 0 and this_val >= heightmap[i - 1][j]:
            continue
        # right
        if i + 1 < size_y and this_val >= heightmap[i + 1][j]:
            continue
        # top
        if j > 0 and this_val >= heightmap[i][j - 1]:
            continue
        # bottom
        if j + 1 < size_x and this_val >= heightmap[i][j + 1]:
            continue
        print(f"Low point found at {i},{j} -> value {this_val}")
        low_point_values.append(this_val)
        low_points.append((i, j))

print(f"The risk level is {sum(1+x for x in low_point_values)}")

def get_basin_from_point(i, j, inc_i, inc_j, visited: Set[str]):
    current = f'{i+inc_i},{j+inc_j}'
    if (i + inc_i) < 0 or (i + inc_i) >= size_y:
        return
    if (j + inc_j) < 0 or (j + inc_j) >= size_x:
        return
    if current in visited:
        return
    if heightmap[i + inc_i][j + inc_j] >= 9:
        return
    # current is okay and unvisited
    visited.add(current)
    if inc_i == 0:
        get_basin_from_point(i + inc_i, j + inc_j, +1, 0, visited)
        get_basin_from_point(i + inc_i, j + inc_j, -1, 0, visited)
    if inc_j == 0:
        get_basin_from_point(i + inc_i, j + inc_j, 0, +1, visited)
        get_basin_from_point(i + inc_i, j + inc_j, 0, -1, visited)
    if inc_i != 0 or inc_j != 0:
        get_basin_from_point(i + inc_i, j + inc_j, inc_i, inc_j, visited) 

basins = []
for i,j in low_points:
    this_group = set() 
    get_basin_from_point(i,j,0,0, this_group)
    print(f'{i},{j} -> {len(this_group)}')
    basins.append(this_group)

basin_sizes = sorted([len(s) for s in basins])
print(f"The results is {basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]}")