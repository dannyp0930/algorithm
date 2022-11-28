dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(i, j, cnt):
    q = [(i, j)]
    arr[i][j] = cnt
    while q:
        r, c = q.pop(0)
        visit[r][c] = 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if arr[nr][nc] == 1 and not visit[nr][nc]:
                arr[nr][nc] = cnt
                q.append((nr, nc))


def bridge(i, j, s):
    for d in range(4):
        cnt = 0
        r, c = i, j
        while 1:
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                break
            if arr[nr][nc] == s:
                break
            if arr[nr][nc]:
                e = arr[nr][nc]
                if cnt > 1:
                    edges.append((s, e, cnt))
                break
            r, c = nr, nc
            cnt += 1


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
island_cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visit[i][j]:
            island_cnt += 1
            bfs(i, j, island_cnt)

edges = []
parent = [i for i in range(island_cnt + 1)]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            bridge(i, j, arr[i][j])
edges.sort(key=lambda x: x[2])
ans = 0
cnt = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
        cnt += 1
        if cnt == island_cnt - 1:
            break
if cnt == island_cnt - 1:
    print(ans)
else:
    print(-1)
