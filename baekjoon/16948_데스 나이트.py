import sys
from collections import deque
input = sys.stdin.readline
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]


N = int(input())
board = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
q = deque([(r1, c1)])
board[r1][c1] = 1
ans = 0
while q:
    r, c = q.popleft()
    if r == r2 and c == c2:
        ans = board[r][c]
        break
    for d in range(6):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
            q.append((nr, nc))
            board[nr][nc] = board[r][c] + 1
print(ans - 1)
