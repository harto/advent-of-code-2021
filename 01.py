with open('inputs/01') as f:
    nums = [int(x) for x in f]

# part 1

incs = 0
prev = None
for n in nums:
    if prev is not None and n > prev:
        incs += 1
    prev = n
print(incs)

# part 2

windows = [nums[i:i+3] for i in range(0, len(nums) - 2)]
incs = 0
prev_sum = None
for w in windows:
    s = sum(w)
    if prev_sum is not None and s > prev_sum:
        incs += 1
    prev_sum = s
print(incs)
