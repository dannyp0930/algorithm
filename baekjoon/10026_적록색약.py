# DFS/BFS

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
Q = []

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# def dfs(r, c):
#     global cnt
#     visit[r][c] = cnt
#     color = arr[r][c]
#
#     for d in range(4):
#         nr, nc = r + dr[d], c + dc[d]
#         if 0 <= nr < N and 0 <= nc < N:
#             if visit[nr][nc] == 0 and arr[nr][nc] == color:
#                 dfs(nr, nc)
#
#


def bfs(r, c):
    global cnt
    Q.append((r, c))
    visit[r][c] = cnt
    while Q:
        r, c = Q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == arr[r][c] and visit[nr][nc] == 0:
                    Q.append((nr, nc))
                    visit[nr][nc] = cnt


cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            cnt += 1
            bfs(i, j)
cnt1 = cnt
for m in range(N):
    for n in range(N):
        if arr[m][n] != 'B':
            arr[m][n] = 'C'
visit = [[0] * N for _ in range(N)]
Q = []

cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            cnt += 1
            bfs(i, j)
cnt2 = cnt
print(cnt1, cnt2)
