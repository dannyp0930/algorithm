n = int(input())
dp = [0, 0, 1, 0, 2, 1]
if n > 5:
    for i in range(6, n + 1):
        tmp = 0
        if dp[i - 2] and dp[i - 5]:
            tmp = min(dp[i - 2], dp[i - 5]) + 1
        elif dp[i - 2] and not dp[i - 5]:
            tmp = dp[i - 2] + 1
        elif not dp[i - 2] and dp[i - 5]:
            tmp = dp[i - 5] + 1
        dp.append(tmp)
if not dp[n]:
    print(-1)
else:
    print(dp[n])
