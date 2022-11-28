n = int(input())
mod = 10007
dp = [1] * 10
for _ in range(n - 1):
    for j in range(1, 10):
        dp[j] = (dp[j] + dp[j - 1]) % mod
print(sum(dp) % mod)
