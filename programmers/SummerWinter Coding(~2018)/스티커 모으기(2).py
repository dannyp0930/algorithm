def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
    ans = 0
    dp1 = sticker[::]
    for i in range(1, n - 1):
        if i == 1:
            dp1[i] = max(dp1[i], dp1[i - 1])
        else:
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])
    dp2 = sticker[::]
    for i in range(2, n):
        if i == 2:
            dp2[i] = max(dp2[i], dp2[i - 1])
        else:
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])
    return max(dp1[n - 2], dp2[n - 1])