from collections import deque
import sys


def bfs(i, j, color):
    global cnt_w, cnt_b
    q = deque([(i, j)])
    cnt = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < M and 0 <= nc < N:
                if not visit[nr][nc] and field[nr][nc] == color:
                    q.append((nr, nc))
                    visit[nr][nc] = 1
                    cnt += 1
    if color == 'W':
        cnt_w += cnt ** 2
    else:
        cnt_b += cnt ** 2


input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
field = [list(input()) for _ in range(M)]
visit = [[0] * N for _ in range(M)]
cnt_w = cnt_b = 0
for r in range(M):
    for c in range(N):
        if not visit[r][c]:
            visit[r][c] = 1
            bfs(r, c, field[r][c])
print(cnt_w, cnt_b)
