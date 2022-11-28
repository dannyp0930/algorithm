import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)
q = int(input())
dp = [[0] * 26 for _ in range(N)]
dp[0][ord(S[0]) - 97] = 1
for i in range(1, N):
    dp[i][ord(S[i]) - 97] = 1
    for j in range(26):
        dp[i][j] += dp[i - 1][j]
for _ in range(q):
    a, l, r = map(str, input().split())
    l, r = int(l), int(r)
    idx = ord(a) - 97
    if l == 0:
        print(dp[r][idx])
    else:
        print(dp[r][idx] - dp[l - 1][idx])