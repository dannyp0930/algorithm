def pow(s, e):
    if s == 0:
        return 2
    elif s == e:
        return 1
    elif abs(s - e) == 2:
        return 4
    else:
        return 3


INF = 0xffffff
arr = list(map(int, input().split()))
n = len(arr)
# 순서, 왼발, 오른발
dp = [[[INF] * 5 for _ in range(5)] for _ in range(n)]
dp[0][0][0] = 0
for i in range(1, n):
    m = arr[i - 1]
    for l in range(5):
        for r in range(5):
            dp[i][m][r] = min(dp[i][m][r], dp[i - 1][l][r] + pow(l, m))
            dp[i][l][m] = min(dp[i][l][m], dp[i - 1][l][r] + pow(r, m))
ans = INF
for lst in dp[n - 1]:
    ans = min(ans, min(lst))
print(ans)
