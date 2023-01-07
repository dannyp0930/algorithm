def bfs():
    while fire:
        r, c = fire.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C:
                if not fires[nr][nc] and arr[nr][nc] != '#':
                    fires[nr][nc] = fires[r][c] + 1
                    fire.append((nr, nc))
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C:
                if not visit[nr][nc] and arr[nr][nc] != '#':
                    if not fires[nr][nc] or fires[nr][nc] > visit[r][c] + 1:
                        visit[nr][nc] = visit[r][c] + 1
                        q.append((nr, nc))
            else:
                return visit[r][c] + 1
    return 'IMPOSSIBLE'


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
R, C = map(int, input().split())
arr = [input() for _ in range(R)]
q = []
visit = [[0] * C for _ in range(R)]
fire = []
fires = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'F':
            fire.append((r, c))
        elif arr[r][c] == 'J':
            q.append((r, c))
print(bfs())
