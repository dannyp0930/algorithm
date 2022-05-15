N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 가로, 세로, 대각
dp = [[[0, 0, 0] for _ in range(N)]for _ in range(N)]
dp[0][1][0] = 1
for i in range(2, N):
    if not arr[0][i]:
        dp[0][i][0] = dp[0][i - 1][0]
for r in range(1, N):
    for c in range(2, N):
        if not arr[r][c] and not arr[r - 1][c] and not arr[r][c - 1]:
            dp[r][c][2] += dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]
        if not arr[r][c]:
            dp[r][c][0] += dp[r][c - 1][0] + dp[r][c - 1][2]
            dp[r][c][1] += dp[r - 1][c][1] + dp[r - 1][c][2]
print(sum(dp[N - 1][N - 1]))
