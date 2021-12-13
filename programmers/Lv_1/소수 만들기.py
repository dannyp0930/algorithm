from itertools import combinations


def determine(x):
    for i in range(2, x):
        if not x % i:
            return False
    return True


def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    for lst in arr:
        if determine(sum(lst)):
            answer += 1
    return answer
