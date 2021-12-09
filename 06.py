# inp = '''
# 3,4,3,1,2
# '''.strip()

with open('inputs/06') as f:
    inp = f.readlines()[0]

from collections import defaultdict

counts = defaultdict(int)

for s in inp.split(','):
    counts[int(s)] += 1

for _ in range(256):
    spawning = counts[0]
    del counts[0]
    for day in range(1, 9):
        counts[day - 1] = counts[day]
    counts[6] += spawning
    counts[8] = spawning

print(sum(counts.values()))
