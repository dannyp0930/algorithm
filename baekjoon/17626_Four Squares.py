import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 50001
dp[1] = 1
for i in range(1, n + 1):
    dp[i] = dp[1] + dp[i - 1]
    for j in range(2, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], 1 + dp[i - j * j])
print(dp[n])
