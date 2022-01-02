FILENAME = "input.txt"
STEPS = 40

rules = {}
with open(FILENAME, "r") as fo:
    template = fo.readline().strip()
    fo.readline()
    for line in fo:
        if not line:
            continue
        a = line.strip().split("->")
        rules[a[0].strip()] = a[1].strip()

pairs = {template[i : i + 2]: 1 for i in range(len(template) - 1)}
letter_counts = {}
for p in template:
    if p not in letter_counts:
        letter_counts[p] = 0
    letter_counts[p] += 1

for step in range(STEPS):
    olds = pairs.copy()
    for pair, count in olds.items():
        if not count:
            continue
        if pair in rules:
            k = rules[pair]
            if k not in letter_counts:
                letter_counts[k] = 0
            letter_counts[k] += count
            for p in (pair[0] + k, k + pair[1]):
                if p not in pairs:
                    pairs[p] = 0
                pairs[p] += count
            pairs[pair] -= count

print(f"After {step+1} steps, the polymer has length {sum(letter_counts.values())}")
print(
    "The highest - lowest count = "
    f"{max(letter_counts.values())-min(letter_counts.values())}"
)
