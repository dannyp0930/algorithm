N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(i, N):
        dp[j - i][j] = 2 ** 32
        for k in range(j - i, j):
            dp[j - i][j] = min(dp[j - i][j], dp[j - i][k] + dp[k + 1][j] + arr[j - i][0] * arr[k][1] * arr[j][1])
print(dp[0][N - 1])
