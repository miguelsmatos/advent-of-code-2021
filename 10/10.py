FILENAME = "input.txt"

OPEN_CLOSE = {"(": ")", "[": "]", "<": ">", "{": "}"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
CLOSING_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}

point_sum = 0
closing_point_list = []

with open(FILENAME, "r") as fo:
    for l, line in enumerate(fo):
        opened = list()
        for c in line:
            illegal = False
            if c in OPEN_CLOSE.keys():
                opened.append(OPEN_CLOSE[c])
            elif c in OPEN_CLOSE.values():
                if opened[-1] != c:
                    print(f"Line {1+l:4}: Expecting {opened[-1]}, but found {c} instead ++ {POINTS[c]}")
                    point_sum += POINTS[c]
                    illegal = True
                    break
                else:
                    del opened[-1]
        if not illegal:
            line_closing_points = 0
            for c in reversed(opened):
                line_closing_points = line_closing_points*5 + CLOSING_POINTS[c]
            closing_point_list.append(line_closing_points)
            print(f'Line {l+1:4} is incomplete: {line_closing_points} closing points --')

closing_point_list.sort()
center = int((len(closing_point_list))/2)

print(f'Sum of illegal points: {point_sum}')
print(f'Middle value of closing points: {closing_point_list[center]}')


