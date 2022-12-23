import sys
from collections import deque


def bfs(i, j):
    q = deque([(i, j)])
    size = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] and not visit[nr][nc]:
                    visit[nr][nc] = 1
                    q.append((nr, nc))
                    size += 1
    return size


input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
paint = []
visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visit[i][j]:
            visit[i][j] = 1
            paint.append(bfs(i, j))
print(len(paint))
if paint:
    print(max(paint))
else:
    print(0)
