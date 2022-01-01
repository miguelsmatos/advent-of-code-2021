import numpy as np

FILENAME = 'input.txt'

counts = {}
ranges = []

with open(FILENAME, 'r') as fo:
    for line in fo:
        try:
            cf, ct = line.split('->')
            i,j = [int(x) for x in cf.split(',')]
            ii,jj = [int(x) for x in ct.split(',')]
            ranges.append([i,j,ii,jj])
        except Exception:
            continue

for ii,jj,iii,jjj in ranges:
    if ii != iii and jj!= jjj:
        continue
    iinc = 1 if ii<iii else -1
    jinc = 1 if jj<jjj else -1
    # print(f'{ii},{jj}->{iii},{jjj}')
    for i in range(ii,iii+iinc,iinc):
        for j in range(jj,jjj+jinc,jinc):
            key = f'{i},{j}'
            if key not in counts:
                counts[key] = 0
            counts[key] += 1

danger = sum(c > 1 for c in counts.values())
print(f'{danger} danger points with >1 visits')


for ii,jj,iii,jjj in ranges:
    iinc = 1 if ii<iii else -1
    jinc = 1 if jj<jjj else -1
    if ii != iii and jj != jjj:
        # print(f'{ii},{jj}->{iii},{jjj}')
        for m,_ in enumerate(range(ii, iii+iinc, iinc)):
            key = f'{ii+iinc*m},{jj+jinc*m}'
            if key not in counts:
                counts[key] = 0
            counts[key] += 1

danger = sum(c > 1 for c in counts.values())
print(f'{danger} danger points with >1 visits')


    