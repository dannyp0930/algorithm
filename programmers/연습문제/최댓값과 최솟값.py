def solution(s):
    nums = list(map(int, s.split(' ')))
    return '{} {}'.format(min(nums), max(nums))
