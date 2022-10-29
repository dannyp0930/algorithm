def dfs(i):
    visit = [False] * (N + 1)
    stack = [i]
    visit[i] = True
    res = []
    while stack:
        u = stack.pop()
        res.append(u)
        v = graph[u]
        if v == i:
            return res
        if visit[v]:
            return []
        stack.append(v)
        visit[v] = True


N = int(input())
graph = [0] + [int(input()) for _ in range(N)]
pick = []
for i in range(1, N + 1):
    if i not in pick:
        for j in dfs(i):
            pick.append(j)
print(len(pick))
pick.sort()
for n in pick:
    print(n)
