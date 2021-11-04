dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(x, y):
    Q.append((x, y))
    while Q:
        r, c = Q.pop()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                arr[nr][nc] = 0
                Q.append((nr, nc))


for T in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    Q = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                bfs(i, j)
                arr[i][j] = 0
                cnt += 1
    print(cnt)
