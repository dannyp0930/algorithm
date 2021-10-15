# DP

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n + 1)]
dp[0] = arr[0]
if n > 1:
    for i in range(1, n):
        for j in range(i + 1):
            tmp = arr[i][j]
            if j == 0:
                tmp += dp[i - 1][0]
            elif j == i:
                tmp += dp[i - 1][i - 1]
            else:
                tmp += max(dp[i - 1][j - 1], dp[i - 1][j])
            dp[i][j] = tmp
print(max(dp[n - 1]))
