FILENAME = "input.txt"

dots = []
folds = []

with open(FILENAME, "r") as fo:
    for line in fo:
        digits = [int(d) for d in line.strip().split(",") if d]
        if digits:
            dots.append(digits)
        else:
            break
    for line in fo:
        if line:
            folds.append(line)


def fold_in_y(dots, y):
    new_dots = []
    for i, j in dots:
        pair = [i, j]
        if j >= y:
            jj = y - (j - y)
            pair = [i, jj]
        if pair not in new_dots:
            new_dots.append(pair)
    return new_dots


def fold_in_x(dots, x):
    new_dots = []
    for i, j in dots:
        pair = [i, j]
        if i >= x:
            ii = x - (i - x)
            pair = [ii, j]
        if pair not in new_dots:
            new_dots.append(pair)
    return new_dots


for fold in folds:
    fold_location = int(fold.split("=")[-1])
    if "along y" in fold:
        dots = fold_in_y(dots, fold_location)
        print(f"{fold.strip().title()} -> dots: {len(dots)}")
    if "along x" in fold:
        dots = fold_in_x(dots, fold_location)
        print(f"{fold.strip().title()} -> dots: {len(dots)}")

max_x = 1 + max(v[0] for v in dots)
max_y = 1 + max(v[1] for v in dots)

print()
array = [["." for _ in range(max_x)] for _ in range(max_y)]
for j, i in dots:
    array[i][j] = "#"
for l in array:
    print("".join(l))
