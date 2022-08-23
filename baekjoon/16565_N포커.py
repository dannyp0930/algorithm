mod = 10007
comb = [[0] * 53 for _ in range(53)]
for n in range(53):
    comb[n][0], comb[n][n] = 1, 1
    for k in range(1, n):
        comb[n][k] = (comb[n - 1][k] + comb[n - 1][k - 1]) % mod
        comb[n][n - k] = comb[n][k]
N = int(input())
i = 1
ans = 0
while 4 * i <= N:
    if i % 2:
        ans += comb[13][i] * comb[52 - 4 * i][N - 4 * i]
    else:
        ans -= comb[13][i] * comb[52 - 4 * i][N - 4 * i]
    ans %= mod
    i += 1
print(ans)
