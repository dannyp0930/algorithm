dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def chese_left():
    for r in range(N):
        for c in range(M):
            if graph[r][c]:
                return True
    return False


def boundary(r, c):
    return 0 <= r < N and 0 <= c < M


def bfs():
    while q:
        r, c = q.pop()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if boundary(nr, nc) and not visit[nr][nc]:
                if graph[nr][nc]:
                    graph[nr][nc] += 1
                else:
                    visit[nr][nc] = 1
                    q.append((nr, nc))

def melt():
    for r in range(N):
        for c in range(M):
            if graph[r][c] > 2:
                graph[r][c] = 0
            elif graph[r][c] == 2:
                graph[r][c] = 1


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while chese_left():
    q = [(0, 0)]
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    bfs()
    melt()
    cnt += 1
print(cnt)
