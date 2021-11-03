# DFS/BFS

dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]


M, N = map(int, input().split())
arr = [[0] * N] + [[0] + list(map(int, input().split())) for _ in range(M)]
sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())
visit = [[[0] * 5 for _ in range(N + 1)] for _ in range(M + 1)] # 방분 배열, visit[r][c][d]
visit[sr][sc][sd] = 1
Q = [(sr, sc, sd)]
while Q:
    r, c, d = Q.pop(0)
    if d == 1 or d == 2:
        d1, d2 = 3, 4
    else:
        d1, d2 = 1, 2
    if not visit[r][c][d1]:
        visit[r][c][d1] = visit[r][c][d] + 1
        Q.append((r, c, d1))
    if not visit[r][c][d2]:
        visit[r][c][d2] = visit[r][c][d] + 1
        Q.append((r, c, d2))
    for k in range(1, 4):
        nr, nc = r + dr[d] * k, c + dc[d] * k
        if nr <= 0 or nc <= 0 or nr > M or nc > N: break
        if arr[nr][nc]: break
        if not visit[nr][nc][d]:
            visit[nr][nc][d] = visit[r][c][d] + 1
            Q.append((nr, nc, d))
print(visit[er][ec][ed] - 1)
