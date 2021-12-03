# inp = '''
# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
# '''.strip().split('\n')

with open('inputs/03') as f:
    inp = f.readlines()

nbits = len(inp[0].strip())
nums = [int(x, 2) for x in inp]

def most_common_bit(xs, i):
    return 1 if sum(1 & x >> i for x in xs) >= len(xs) / 2 else 0

# part 1

mcbs = 0
for i in range(nbits):
    mcbs |= most_common_bit(nums, i) << i

lcbs = ((1 << nbits) - 1) ^ mcbs

print(mcbs * lcbs)

# part 2

orig_nums = nums[:]

for i in range(nbits - 1, -1, -1):
    if len(nums) == 1: break
    mcb = most_common_bit(nums, i)
    nums = [n for n in nums if n & (1 << i) == (mcb << i)]

o2_gen_rating = nums[0]

nums = orig_nums[:]

for i in range(nbits - 1, -1, -1):
    if len(nums) == 1: break
    lcb = most_common_bit(nums, i) ^ 1
    nums = [n for n in nums if n & (1 << i) == (lcb << i)]

co2_scrubber_rating = nums[0]

print(o2_gen_rating * co2_scrubber_rating)
