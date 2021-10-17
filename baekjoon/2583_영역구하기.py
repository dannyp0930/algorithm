# DFS/BFS

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            arr[r][c] = 1
space = []
for i in range(M):
    for j in range(N):
        if i < 0 or i >= M or j < 0 or j >= N or arr[i][j]: continue
        Q = [(i, j)]
        arr[i][j] = 1
        cnt = 1
        while Q:
            r, c = Q.pop(0)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr < 0 or nr >= M or nc < 0 or nc >= N or arr[nr][nc]: continue
                arr[nr][nc] = 1
                cnt += 1
                Q.append((nr, nc))
        space.append(cnt)
space.sort()
print(len(space))
print(*space)
