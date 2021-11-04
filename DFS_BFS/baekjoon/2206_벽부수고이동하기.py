dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
    while Q:
        r, c, s = Q.pop(0)
        if r == N - 1 and c == M - 1:
            return visit[r][c][s]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and s == 1:
                    visit[nr][nc][0] = visit[r][c][1] + 1
                    Q.append((nr, nc, 0))
                elif arr[nr][nc] == 0 and visit[nr][nc][s] == 0:
                    visit[nr][nc][s] = visit[r][c][s] + 1
                    Q.append((nr, nc, s))
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
Q = [(0, 0, 1)]
visit[0][0][1] = 1
print(bfs())
