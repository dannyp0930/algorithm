def calc(i, l, r):
    j = abs(l - r)
    if j not in arr:
        arr.append(j)
    if i == n:
        return
    if not dp[i][j]:
        calc(i + 1, l, r)
        calc(i + 1, l + weights[i], r)
        calc(i + 1, l, r + weights[i])
        dp[i][j] = 1


n = int(input())
weights = list(map(int, input().split()))
dp = [[0] * 150001 for _ in range(n + 1)]
arr = []
calc(0, 0, 0)
m = int(input())
beeds = list(map(int, input().split()))
for b in beeds:
    if b in arr:
        print('Y', end=' ')
    else:
        print('N', end=' ')
