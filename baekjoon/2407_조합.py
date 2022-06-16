import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dp = [0] * (m + 1)
dp[0] = 1
for i in range(1, m + 1):
    dp[i] = dp[i - 1] * (n - i + 1) // i
print(dp[m])