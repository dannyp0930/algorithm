# DP

import sys
sys.stdin = open('3282.txt', 'r')

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    V = [0]
    C = [0]
    for _ in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for v in range(1, K + 1):
            if V[i] > v:
                dp[i][v] = dp[i - 1][v]
            else:
                dp[i][v] = max(dp[i - 1][v], C[i] + dp[i - 1][v - V[i]])
    print('#{} {}'.format(T, dp[N][K]))
