from math import sqrt


def solution(k, d):
    ans = 0
    for a in range(0, d + 1, k):
        b = sqrt(d ** 2 - a ** 2)
        ans += b // k + 1
    return ans
