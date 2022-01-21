energy_levels = {}

def init():
    for y, row in enumerate('''
        8577245547
        1654333653
        5365633785
        1333243226
        4272385165
        5688328432
        3175634254
        6775142227
        6152721415
        2678227325
    '''.strip().split('\n')):
        for x, c in enumerate(row.strip()):
            energy_levels[x, y] = int(c)

def step():
    for k, v in energy_levels.items():
        energy_levels[k] += 1

    flashed = set()
    flash = [k for k, v in energy_levels.items() if v > 9]
    while flash:
        k = flash.pop()
        if k in flashed: continue
        flashed.add(k)
        neighbors = [(k[0] + dx, k[1] + dy)
                      for dx in (-1, 0, 1)
                      for dy in (-1, 0, 1)
                      if not (dx == 0 and dy == 0)]
        for n in neighbors:
            if n not in energy_levels: continue
            energy_levels[n] += 1
            if energy_levels[n] > 9:
                flash.append(n)

    for k in flashed:
        energy_levels[k] = 0

    return len(flashed)

init()
total_flashes = 0
for i in range(100):
    total_flashes += step()

print(total_flashes)

init()
steps = 1
while True:
    if step() == 100:
        print(steps)
        break
    steps += 1
