def bfs(i, j):
    q = [(i, j)]
    visit[i][j] = 1
    size = 1
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] and not visit[nr][nc]:
                    q.append((nr, nc))
                    visit[nr][nc] = 1
                    size += 1
    return size


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1
visit = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visit[i][j]:
            ans = max(ans, bfs(i, j))
print(ans)
