N = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]
check = (1 << 10) - 1
mod = 1000000000
for i in range(1, 10):
    dp[1][i][1 << i] = 1
for i in range(2, N + 1):
    for j in range(10):
        for k in range(check + 1):
            bit = k | (1 << j)
            if j == 0:
                dp[i][j][bit] += dp[i - 1][j + 1][k]
            elif j == 9:
                dp[i][j][bit] += dp[i - 1][j - 1][k]
            else:
                dp[i][j][bit] += dp[i - 1][j - 1][k] + dp[i - 1][j + 1][k]
ans = 0
for i in range(10):
    ans += dp[N][i][check]
print(ans % mod)