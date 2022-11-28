N, K = map(int, input().split())
q = [N]
visit = [-1] * 100001
visit[N] = 0
while q:
    p = q.pop(0)
    if p == K:
        break
    for np in [p - 1, p + 1, p * 2]:
        if 0 <= np <= 100000 and visit[np] == -1:
            q.append(np)
            visit[np] = p
res = [K]
while 1:
    if K == N:
        break
    res.append(visit[K])
    K = visit[K]
print(len(res) - 1)
print(*res[::-1])
