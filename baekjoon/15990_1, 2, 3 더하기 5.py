N = 100001
mod = 1000000009
dp = [[0] * 4 for _ in range(N)]
dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1
for i in range(4, N):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % mod
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % mod
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % mod
for _ in range(int(input())):
    n = int(input())
    print(sum(dp[n]) % mod)
