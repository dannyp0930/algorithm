def solution(nums):
    N = len(nums) // 2
    set_nums = set(nums)
    if len(set_nums) > N:
        answer = N
    else:
        answer = len(set_nums)
    return answer
