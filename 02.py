# inp = '''forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2'''.split('\n')

with open('inputs/02') as f:
    inp = f.readlines()

# part 1

x = 0
y = 0

with open('inputs/02') as f:
    for line in f:
        cmd, arg = line.split(' ')
        n = int(arg)
        if cmd == 'forward':
            x += n
        elif cmd == 'down':
            y += n
        elif cmd == 'up':
            y -= n

print(x * y)

# part 2

x = 0
y = 0
aim = 0

for line in inp:
    cmd, arg = line.split(' ')
    n = int(arg)
    if cmd == 'forward':
        x += n
        y += aim * n
    elif cmd == 'down':
        aim += n
    elif cmd == 'up':
        aim -= n

print(x * y)
