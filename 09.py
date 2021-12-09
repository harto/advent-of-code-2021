with open('inputs/09') as f:
    M = [[int(c) for c in line.strip()] for line in f]

def neighbors(x, y):
    return [(x + dx, y + dy)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
            if 0 <= (y + dy) < len(M)
            and 0 <= (x + dx) < len(M[y + dy])]

low_points = [(x, y)
              for y, row in enumerate(M)
              for x, height in enumerate(row)
              if height < min(M[ny][nx] for nx, ny in neighbors(x, y))]

print(sum(M[y][x] + 1 for x, y in low_points))

basins = []
for p in low_points:
    basin = set()
    queue = [p]
    while queue:
        p = queue.pop(0)
        basin.add(p)
        for x, y in neighbors(*p):
            if (x, y) not in basin and M[y][x] < 9:
                queue.append((x, y))
    basins.append(basin)

from functools import reduce
print(reduce(lambda x, y: x * y, (len(b) for b in sorted(basins, key=len)[-3:])))
