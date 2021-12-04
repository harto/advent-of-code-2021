# lines = '''
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# '''.strip().split('\n')

with open('inputs/04') as f:
    lines = [l.strip() for l in f]

numbers = [int(s) for s in lines[0].split(',')]

boards = [
    [[[int(s), False] for s in line.split()] for line in lines[n:n+5]]
    for n in range(2, len(lines), 6)
]

winning_boards = []

for n in numbers:
    for board in boards:
        if board in winning_boards: continue
        for row in board:
            for x, col in enumerate(row):
                if col[0] == n:
                    col[1] = True
                    if all(other_row[x][1] for other_row in board) or \
                       all(other_col[1] for other_col in row):
                        winning_boards.append(board)
                        if len(winning_boards) == len(boards):
                            # find unmarked values
                            unmarked = sum(col[0]
                                           for row in board
                                           for col in row
                                           if not col[1])
                            print(unmarked * n)
                            exit()

