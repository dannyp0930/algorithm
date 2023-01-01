N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j]:
                continue
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
ans = 0
for i in range(1, N + 1):
    tmp = 0
    for j in range(1, N + 1):
        tmp += graph[i][j] + graph[j][i]
    if tmp == N - 1:
        ans += 1
print(ans)
