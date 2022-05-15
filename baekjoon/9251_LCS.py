str1, str2 = input(), input()
l1, l2 = len(str1), len(str2)
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(l1 + 1):
    for j in range(l2 + 1):
        if not i or not j: continue
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[l1][l2])
