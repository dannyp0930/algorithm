N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1):
        dp[j] = max(dp[j], dp[j - i] + P[i])
print(dp[N])
