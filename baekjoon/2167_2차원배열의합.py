N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
for r in range(1, N + 1):
    for c in range(1, M + 1):
        dp[r][c] = dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1] + arr[r - 1][c - 1]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    ans = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
    print(ans)
