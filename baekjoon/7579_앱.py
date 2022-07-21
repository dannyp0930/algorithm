N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
C = sum(cost)
dp = [[0] * (C + 1) for _ in range(N + 1)]
res = C
for i in range(1, N + 1):
    m = memory[i - 1]
    c = cost[i - 1]
    for j in range(1, C + 1):
        if c > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - c] + m, dp[i - 1][j])
        if dp[i][j] >= M:
            res = min(res, j)
print(res)
