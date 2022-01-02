FILENAME = 'sample.txt'
STEPS = 40

rules = {}
with open(FILENAME, 'r') as fo:
    template = fo.readline().strip()
    fo.readline()
    for line in fo:
        if not line:
            continue
        a = line.strip().split('->')
        rules[a[0].strip()] = a[1].strip()

for step in range(STEPS):
    insertions = []
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair in rules:
            insertions.append((i+1, rules[pair]))
    for position, letter in reversed(insertions):
        template = template[0:position] + letter + template[position:]

print(f"After {step+1} the length is {len(template)}")

counts = {}
for c in template:
    if c not in counts:
        counts[c] = 0
    counts[c] += 1

print(f'The highest count - lowest count is {max(counts.values())-min(counts.values())}')