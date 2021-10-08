# DP

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
dp[1] = stairs[1]
if N > 1:
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, N + 1):
        tmp = 0
        if dp[i - 2] > dp[i - 3] + stairs[i - 1]:
            tmp = dp[i - 2]
        else:
            tmp = dp[i - 3] + stairs[i - 1]
        dp[i] = stairs[i] + tmp
print(dp[N])
