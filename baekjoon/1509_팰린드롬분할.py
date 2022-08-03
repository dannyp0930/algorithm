string = input()
N = len(string)
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N - 1):
    if string[i] == string[i + 1]:
        dp[i][i + 1] = 1
for l in range(2, N):
    for i in range(N - l):
        if string[i] == string[i + l] and dp[i + 1][i + l - 1]:
            dp[i][i + l] = 1
P = [0] * (N + 1)
P[1] = 1
for i in range(2, N + 1):
    P[i] = P[i - 1] + 1
    for j in range(1, i):
        if dp[j - 1][i - 1]:
            P[i] = min(P[i], P[j - 1] + 1)
print(P[N])