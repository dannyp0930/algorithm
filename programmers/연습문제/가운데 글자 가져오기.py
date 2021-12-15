def solution(s):
    N = len(s)
    return s[N // 2] if N % 2 else s[N // 2 - 1: N // 2 + 1]
