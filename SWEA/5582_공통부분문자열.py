# DP

str1, str2 = input(), input()
l1, l2 = len(str1), len(str2)
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
ans = 0
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])
print(ans)
