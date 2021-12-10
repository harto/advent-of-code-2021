with open('inputs/10') as f:
    inp = f.readlines()

delims = {'{': '}', '(': ')', '[': ']', '<': '>'}

illegal_chars = []
line_completions = []

for line in inp:
    stack = []
    for c in line.strip():
        if c in delims:
            stack.append(delims[c])
        else:
            if c != stack.pop():
                illegal_chars.append(c)
                break
    else:
        if stack:
            line_completions.append(list(reversed(stack)))

illegal_char_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
print(sum(illegal_char_scores[c] for c in illegal_chars))

extra_char_scores = {')': 1, ']': 2, '}': 3, '>': 4}
from functools import reduce
scores = [
    reduce(lambda score, c: score * 5 + extra_char_scores[c], chars, 0)
    for chars in line_completions
]
scores.sort()
print(scores[len(scores) // 2])
