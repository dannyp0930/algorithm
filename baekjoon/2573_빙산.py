def melt():

    def bfs(i, j):
        q = [(i, j)]
        visit[i][j] = 1
        icebergs.append((i, j))
        while q:
            r, c = q.pop(0)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == 0:
                        visit[r][c] += 1
                    if arr[nr][nc] and not visit[nr][nc]:
                        q.append((nr, nc))
                        visit[nr][nc] = 1
                        icebergs.append((nr, nc))

    time = 0
    while 1:
        visit = [[0] * M for _ in range(N)]
        icebergs = []
        cnt = 0
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j] and not visit[i][j]:
                    bfs(i, j)
                    cnt += 1
        for r, c in icebergs:
            arr[r][c] -= (visit[r][c] - 1)
            if arr[r][c] < 0:
                arr[r][c] = 0
        if cnt == 0:
            return 0
        if cnt > 1:
            return time
        time += 1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(melt())
