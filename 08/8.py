FILENAME = "sample.txt"
FILENAME = "input.txt"

cyphers = []
msgs = []


def contains(a, b) -> bool:
    for ch_b in b:
        if ch_b not in a:
            return False
    return True


def count_overlaps(a, b) -> int:
    c = 0
    for ch_b in b:
        if ch_b in a:
            c += 1
    return c


def sortWord(word) -> str:
    return "".join(sorted(word))


with open(FILENAME, "r") as fo:
    for line in fo:
        try:
            cypher, msg = line.split("|")
            cyphers.append([c for c in cypher.split()])
            msgs.append([m for m in msg.split()])
        except Exception:
            continue

easy_numbers = {
    1: "cf",
    4: "bcdf",
    7: "acf",
    8: "abcdefg",
}

easy_count = 0
for msg in msgs:
    for digit in msg:
        for e in easy_numbers.values():
            if len(digit) == len(e):
                easy_count += 1

print(f"There are {easy_count} simple digits on the output")


def find_cypher(cypher):
    cypher_set = {c for c in cypher}
    cypher_map = {}
    for n, v in easy_numbers.items():
        for c in cypher_set.copy():
            if len(c) == len(v):
                cypher_map[n] = c
                cypher_set.remove(c)
    # 3 must contain 1; 9 must contain 4
    for c in cypher_set.copy():
        if len(c) == 5 and contains(c, cypher_map[1]):
            cypher_map[3] = c
            cypher_set.remove(c)
        if len(c) == 6 and contains(c, cypher_map[4]):
            cypher_map[9] = c
            cypher_set.remove(c)
    # 0 must contain 1;
    for c in cypher_set.copy():
        if len(c) == 6:
            if contains(c, cypher_map[1]):
                cypher_map[0] = c
                cypher_set.remove(c)
            else:
                cypher_map[6] = c
                cypher_set.remove(c)
    # 2 and 5
    for c in cypher_set.copy():
        if len(c) == 5:
            if count_overlaps(cypher_map[6], c) == 5:
                cypher_map[5] = c
                cypher_set.remove(c)
            else:
                cypher_map[2] = c
                cypher_set.remove(c)
    assert len(cypher_set) == 0
    return {sortWord(v): k for k, v in cypher_map.items()}


accum = 0
for i, cypher in enumerate(cyphers):
    cypher_map = find_cypher(cypher)
    msg = int("".join(f"{cypher_map[sortWord(d)]}" for d in msgs[i]))
    accum += msg

print(f"The sum of all lines is {accum}")


# cypher = [
#     "acedgfb",
#     "cdfbe",
#     "gcdfa",
#     "fbcad",
#     "dab",
#     "cefabd",
#     "cdfgeb",
#     "eafb",
#     "cagedb",
#     "ab",
# ]

# print(find_cypher(cypher))
