import sys

input = sys.stdin.readline
expression = input().rstrip().split('-')
nums = []
for num in expression:
    nums.append(sum(list(map(int, num.split('+')))))
print(nums[0] - sum(nums[1:]))