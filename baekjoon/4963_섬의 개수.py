dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visit[i][j] == 0:
                ans += 1
                q = [(i, j)]
                visit[i][j] = 1
                while q:
                    r, c = q.pop(0)
                    for d in range(8):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < h and 0 <= nc < w and graph[nr][nc] == 1 and visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            q.append((nr, nc))
    print(ans)
