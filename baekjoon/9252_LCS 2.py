str1, str2 = input(), input()
l1, l2 = len(str1), len(str2)
dp = [[''] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
        else:
            if len(dp[i][j - 1]) > len(dp[i - 1][j]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
print(len(dp[l1][l2]))
print(dp[l1][l2])
