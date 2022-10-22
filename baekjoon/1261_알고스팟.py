dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
M, N = map(int, input().split())
arr = [input() for _ in range(N)]
visit = [[-1] * M for _ in range(N)]
q = [(0, 0)]
visit[0][0] = 0
while q:
    r, c = q.pop(0)
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < N and 0 <= nc < M): continue
        if visit[nr][nc] != -1: continue
        if arr[nr][nc] == '1':
            visit[nr][nc] = visit[r][c] + 1
            q.append((nr, nc))
        else:
            visit[nr][nc] = visit[r][c]
            q.insert(0, (nr, nc))
print(visit[N - 1][M - 1])
