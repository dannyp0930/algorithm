N = int(input())
max_size = 1000001
dp = [0] * max_size
visit = [0] * max_size
q = [N]
dp[N] = [N]
visit[N] = 1
while q:
    x = q.pop(0)
    if x == 1:
        break
    for i, nx in enumerate([x // 3, x // 2, x - 1]):
        if i == 0 and x % 3: continue
        if i == 1 and x % 2: continue
        if nx and not visit[nx]:
            q.append(nx)
            dp[nx] = dp[x] + [nx]
            visit[nx] = 1
print(len(dp[1]) - 1)
print(*dp[1])
