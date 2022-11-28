N, M = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(1, M + 1):
    w, v = map(int, input().split())
    for j in range(1, N + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[M][N])
