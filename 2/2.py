FILENAME = "sample.txt"
FILENAME = "input.txt"

horizontal = 0
depth = 0
aim = 0

with open(FILENAME, 'r') as fp:
    for line in fp:
        try:
            direction_str, quantity_str = line.strip().split(' ')
            quantity = int(quantity_str)
            direction = direction_str.strip().lower()
            if direction == 'forward':
                horizontal += quantity
                depth += aim * quantity
            elif direction == 'up':
                #depth -= quantity
                aim -= quantity
            elif direction == 'down':
                #depth += quantity
                aim += quantity
            else: 
                raise BaseException(f"Not sure what to do with {quantity}")
        except Exception:
            continue

print(f'After instructions, horizontal postion = {horizontal}, depth = {depth}')
print(f'Multiplying horizontal x depth = {horizontal * depth}')