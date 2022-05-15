from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                Q.append([nr, nc])
                arr[nr][nc] = arr[r][c] + 1


M, N = map(int, input().split())
arr = []
Q = deque([])
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i, j))
bfs()
ans = 0
for lst in arr:
    for num in lst:
        if num == 0:
            print(-1)
            exit(0)
        if ans < num - 1:
            ans = num - 1
print(ans)
