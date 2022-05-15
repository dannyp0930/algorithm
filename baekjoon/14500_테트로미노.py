dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c, total, cnt):
    global ans
    if cnt == 4:
        ans = max(ans, total)
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc]:
            if cnt == 2:
                visit[nr][nc] = 1
                dfs(r, c, total + arr[nr][nc], cnt + 1)
                visit[nr][nc] = 0
            visit[nr][nc] = 1
            dfs(nr, nc, total + arr[nr][nc], cnt + 1)
            visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visit[i][j] = 0
print(ans)
