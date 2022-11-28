import sys

input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
R, C = len(str1), len(str2)
dp = [[''] * C for _ in range(R)]
flag = False
for i in range(1, R):
    if str2[0] == str1[i] or flag:
        dp[i][0] = str2[0]
        flag = True
flag = False
for j in range(1, C):
    if str1[0] == str2[j] or flag:
        dp[0][j] = str1[0]
        flag = True
for r in range(1, R):
    for c in range(1, C):
        if str1[r] == str2[c]:
            dp[r][c] = dp[r - 1][c - 1] + str1[r]
        else:
            if len(dp[r - 1][c]) < len(dp[r][c - 1]):
                dp[r][c] = dp[r][c - 1]
            else:
                dp[r][c] = dp[r - 1][c]
print(dp[R - 1][C - 1])
