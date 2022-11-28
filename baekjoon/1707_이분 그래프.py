def bfs(s, g):
    q = [s]
    visit[s] = g
    while q:
        n = q.pop(0)
        for u in graph[n]:
            if not visit[u]:
                q.append(u)
                visit[u] = -visit[n]
            elif visit[u] == visit[n]:
                return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    flag = True
    for i in range(1, V + 1):
        if not visit[i]:
            if not bfs(i, 1):
                flag = False
                break
    print('YES' if flag else 'NO')
    