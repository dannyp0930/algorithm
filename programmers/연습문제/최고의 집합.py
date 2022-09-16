def solution(n, s):
    share = s // n
    if not share:
        return [-1]
    res = s % n
    ans = [share] * n
    for i in range(res):
        ans[n - i - 1] += 1
    return ans