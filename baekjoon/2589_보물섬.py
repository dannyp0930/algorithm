# DFS/BFS

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
    global cnt
    front = -1
    rear = 0
    while front != rear:
        front += 1
        r, c = Q[front]
        Q[front] = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
            if arr[nr][nc] or visit[nr][nc]: continue
            visit[nr][nc] = visit[r][c] + 1
            cnt = visit[nr][nc]
            rear += 1
            Q[rear] = (nr, nc)


N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(M):
        if tmp[j] == 'W':
            arr[i][j] = 1
ans = 0
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            cnt = 0
            visit = [[0] * M for _ in range(N)]
            Q = [0] * N * M
            Q[0] = (i, j)
            visit[i][j] = 1
            bfs()
            if ans < cnt:
                ans = cnt
print(ans - 1)
