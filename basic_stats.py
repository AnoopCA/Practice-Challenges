import sys

data = sys.stdin.read().strip().split('\n')
n = int(data[0])
nums = list(map(int, data[1].split()))

# Mean
mean = round((sum(nums)/n), 1)

# Median
nums.sort()
if (n%2 != 0):
    median = nums[int(n/2)]
else:
    median = (nums[int(n/2)-1] + nums[int(n/2)]) / 2
median = round(median, 1)

# Mode
nums_counts = {}
for i in range(n):
    if (i != (n-1)) and (i != (n-2)):
        if nums[i] == nums[i+1]:
            if nums[i] in nums_counts:
                nums_counts[nums[i]] = nums_counts[nums[i]] + 1
            else:
                nums_counts[nums[i]] = 2
if nums_counts:
    mode = sorted(nums_counts.items(), key=lambda x:x[1], reverse=True)
    mode = mode[0][0]
else:
    mode = min(nums)

# Standard Deviation
variance = sum((i-mean)**2 for i in nums) / n
std_dev = round(variance**0.5, 1)

#Confidence Interval
ci_lower = mean - (1.96 * (std_dev / (n**0.5)))
ci_upper = mean + (1.96 * (std_dev / (n**0.5)))
ci_lower = round(ci_lower, 1)
ci_upper = round(ci_upper, 1)

print(mean)
print(median)
print(mode)
print(std_dev)
print(f'{ci_lower} {ci_upper}')
