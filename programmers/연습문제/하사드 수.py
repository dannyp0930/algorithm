def solution(x):
    sum_x = sum([int(i) for i in str(x)])
    if x % sum_x:
        return False
    return
