# DFS/BFS

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global ans
    dist = [[-1] * N for _ in range(N)] # 다리를 건설할 리스트
    q = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == n:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        a, b = q.pop(0)
        for k in range(4):
            na, nb = a + dr[k], b + dc[k]
            if na < 0 or nb < 0 or na >= N or nb >= N: continue
            if arr[na][nb] and arr[na][nb] != n: # 다른 섬을 만나는 경우
                if ans > dist[a][b]:
                    ans = dist[a][b]
                return
            if not arr[na][nb] and dist[na][nb] == -1:  # 바다를 만나면
                dist[na][nb] = dist[a][b] + 1
                q.append((na, nb))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
candi = []
cnt = 0
for r in range(N):
    for c in range(N):
        if not visit[r][c] and arr[r][c] == 1:
            cnt += 1
            Q = [(r, c)]
            visit[r][c] = 1
            arr[r][c] = cnt
            while Q:
                x, y = Q.pop(0)
                for d in range(4):
                    nx, ny = x + dr[d], y + dc[d]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
                    if arr[nx][ny] != 1: continue
                    if visit[nx][ny]: continue
                    visit[nx][ny] = 1
                    arr[nx][ny] = cnt
                    Q.append((nx, ny))
ans = N * N
for n in range(1, cnt + 1):
    bfs()
print(ans)
