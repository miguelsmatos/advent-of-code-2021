from typing import List

FILENAME = 'input.txt'
STEPS = 1000 # change to 100 for the first part

grid = []
with open(FILENAME, 'r') as fo:
    for line in fo:
        grid.append([int(d) for d in line if d.isdigit()])


def start_step(grid: List[List[int]]):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1

def find_flashes(grid):
    coordinates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 10:
                coordinates.append((i,j))
    return coordinates

def flash_energy(grid, i, j):
    for ii in range(-1,2):
        for jj in range(-1,2):
            iii, jjj = i+ii, j+jj
            if iii>=0 and iii < len(grid) and jjj>=0 and jjj < len(grid[iii]):
                if grid[iii][jjj] <= 9 and grid[iii][jjj] != 0:
                    grid[iii][jjj] += 1

flash_count: int = 0
for s in range(STEPS):
    start_step(grid)
    step_flash_count = 0
    flashes = find_flashes(grid)
    while flashes:
        for i,j in flashes:
            step_flash_count += 1
            grid[i][j] = 0
            flash_energy(grid,i,j)
        flashes = find_flashes(grid)
    flash_count += step_flash_count
    if (step_flash_count == len(grid)*len(grid[0])):
        print(f'All flashed at step {s+1}')
        break
    
print(f'After {s+1} steps there were {flash_count} flashes')