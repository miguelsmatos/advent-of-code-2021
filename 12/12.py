FILENAME = "input.txt"
ALLOW_TWO_VISITS_ONCE = True  # Change to False for Part 1

roads = []
with open(FILENAME, "r") as fo:
    for line in fo:
        roads.append([x for x in line.strip().split("-") if x])

# add reverse and fix directions
for r in range(len(roads)):
    if roads[r][1] == "start":
        roads[r] = roads[r][::-1]
    if roads[r][0] == "end":
        roads[r] = roads[r][::-1]
    if roads[r][0] != "start" and roads[r][1] != "end":
        roads.append([roads[r][1], roads[r][0]])


def is_path_valid(path):
    lower_visited = {}
    for p in path:
        if p == "start":
            continue
        if p == "end":
            return True
        if p.islower():
            if p in lower_visited:
                if ALLOW_TWO_VISITS_ONCE:
                    if sum(v >= 2 for v in lower_visited.values()) >= 1:
                        return False  # There is already 1 duplicate
                    lower_visited[p] += 1
                else:
                    return False
            else:
                lower_visited[p] = 1

    return True


active_paths = [r for r in roads if r[0] == "start"]
has_changed = True
while has_changed:
    has_changed = False
    new_paths = []
    for road_start, road_end in roads:
        for path in active_paths:
            if road_start == path[-1]:
                new_path = path + [road_end]
                if is_path_valid(new_path):
                    new_paths.append(new_path)
                    has_changed = True
    # valid paths
    active_paths = [p for p in active_paths if p[-1] == "end"] + new_paths

print(f"Total of valid paths: {len(active_paths)}")
