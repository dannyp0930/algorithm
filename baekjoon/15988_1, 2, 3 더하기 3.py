N = 1000000
mod = 1000000009
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    for j in range(1, 4):
        if i - j < 0:
            break
        dp[i] += dp[i - j]
    dp[i] %= mod
for _ in range(int(input())):
    n = int(input())
    print(dp[n])
