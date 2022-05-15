N = int(input())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(3)] for _ in range(N + 1)]for _ in range(N + 1)]
dp[1][2][0] = 1
for i in range(3, N + 1):
    if not arr[1][i]:
        dp[1][i][0] = dp[1][i - 1][0]
for r in range(2, N + 1):
    for c in range(2, N + 1):
        if not arr[r][c] and not arr[r - 1][c] and not arr[r][c - 1]:
            dp[r][c][1] += dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]
        if not arr[r][c]:
            dp[r][c][0] += dp[r][c - 1][0] + dp[r][c - 1][1]
            dp[r][c][2] += dp[r - 1][c][1] + dp[r - 1][c][2]
print(sum(dp[N][N]))
