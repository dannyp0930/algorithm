gears = [input() for _ in range(4)]
K = int(input())
ans = 0
for _ in range(K):
    a, b = map(int, input().split())
    visit = [0] * 4
    q = [a - 1]
    visit[a - 1] = b
    while q:
        g = q.pop(0)
        if g + 1 < 4 and not visit[g + 1]:
            if gears[g][2] != gears[g + 1][6]:
                visit[g + 1] = -visit[g]
                q.append(g + 1)
        if g - 1 >= 0 and not visit[g - 1]:
            if gears[g][6] != gears[g - 1][2]:
                visit[g - 1] = -visit[g]
                q.append(g - 1)
    for i, v in enumerate(visit):
        if v == 1:
            gears[i] = gears[i][-1] + gears[i][:-1]
        elif v == -1:
            gears[i] = gears[i][1:] + gears[i][0]
for i, g in enumerate(gears):
    if g[0] == '1':
        ans += 2 ** i
print(ans)
