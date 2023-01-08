V, E = map(int, input().split())
INF = float('inf')
graph = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c, = map(int, input().split())
    graph[a][b] = c
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
ans = INF
for i in range(1, V + 1):
    ans = min(ans, graph[i][i])
if ans != INF:
    print(ans)
else:
    print(-1)