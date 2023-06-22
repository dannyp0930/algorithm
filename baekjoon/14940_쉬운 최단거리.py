dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int, input().split())
x, y = 0, 0
graph = []
visit = [[-1] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 2:
            x, y = i, j
        elif tmp[j] == 0:
            visit[i][j] = 0
q = [(x, y)]
visit[x][y] = 0
while q:
    r, c = q.pop(0)
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m:
            if graph[nr][nc] == 1 and visit[nr][nc] == -1:
                visit[nr][nc] = visit[r][c] + 1
                q.append((nr, nc))
for lst in visit:
    print(*lst)
