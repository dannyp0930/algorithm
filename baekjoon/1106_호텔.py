C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [100000] * (C + 100)
dp[0] = 0
for cost, val in arr:
    for i in range(val, C + 100):
        dp[i] = min(dp[i], dp[i - val] + cost)
print(min(dp[C:]))
