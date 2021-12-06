# inp = '''
# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# '''.strip().split('\n')

with open('inputs/05') as f:
    inp = f.readlines()

from collections import defaultdict
import re

counts = defaultdict(int)

def covered_points(x1, y1, x2, y2):
    dx = 1 if x2 > x1 else -1 if x2 < x1 else 0
    dy = 1 if y2 > y1 else -1 if y2 < y1 else 0
    x = x1
    y = y1
    while True:
        yield (x, y)
        if x == x2 and y == y2: return
        x += dx
        y += dy

for line in inp:
    x1, y1, x2, y2 = [int(g) for g in re.match('(\d+),(\d+) -> (\d+),(\d+)', line).groups()]
    for p in covered_points(x1, y1, x2, y2):
        counts[p] += 1

print(len([v for v in counts.values() if v > 1]))
