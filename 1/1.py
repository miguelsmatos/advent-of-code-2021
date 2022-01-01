from typing import Optional, List

FILENAME = "input.txt"

previous: Optional[int] = None
increase_count = 0
measurements: List[int] = []
with open(FILENAME, "r") as fp:
    for line in fp:
        try:
            current = float(line)
            measurements.append(current)
        except Exception:
            continue
        if previous is None:
            previous = current
            continue
        increase_count += current > previous
        previous = current

line_count = len(measurements)
print(f"Found {increase_count} increases; {line_count} relevant lines")

previous = None
count_range = 3
sampled_count = 0
increase_count = 0
for i, current in enumerate(measurements):
    if not (i + count_range - 1 < len(measurements)):
        break
    current = sum((measurements[i + j] for j in range(count_range)))
    sampled_count += 1
    if previous is None:
        previous = current
        continue
    increase_count += current > previous
    previous = current

print(f"Found {increase_count} increases; {sampled_count} relevant groups")
