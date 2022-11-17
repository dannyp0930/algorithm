def dfs(n, cnt):
    global ans
    if cnt == 4:
        ans = 1
        return
    visit[n] = 1
    for v in graph[n]:
        if not visit[v]:
            visit[v] = 1
            dfs(v, cnt + 1)
            visit[v] = 0


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visit = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = 0
for i in range(N):
    dfs(i, 0)
    visit[i] = 0
    if ans:
        break
print(ans)
