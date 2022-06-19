import sys

input = sys.stdin.readline
N, K = map(int, input().split())
W = [0] * (N + 1)
V = [0] * (N + 1)
for n in range(1, N + 1):
    w, v = map(int, input().split())
    W[n] = w
    V[n] = v
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for k in range(1, K + 1):
        if W[i] > k:
            dp[i][k] = dp[i - 1][k]
        else:
            dp[i][k] = max(dp[i - 1][k - W[i]] + V[i], dp[i - 1][k])
print(dp[N][K])
