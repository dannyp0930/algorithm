import sys
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
    q = deque([(0, 0, 0)])
    visit[0][0][0] = 1

    while q:
        r, c, w = q.popleft()
        if r == N - 1 and c == M - 1:
            return visit[r][c][w]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc][w] == 0:
                if arr[nr][nc] == 0:
                    q.append((nr, nc, w))
                    visit[nr][nc][w] = visit[r][c][w] + 1
                elif w == 0:
                    q.append((nr, nc, 1))
                    visit[nr][nc][1] = visit[r][c][w] + 1
    return -1

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(bfs())
