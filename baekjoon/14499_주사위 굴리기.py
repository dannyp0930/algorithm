import sys


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))
t = 0
b = 0
e = 0
w = 0
s = 0
n = 0
for i in range(K):
    d = C[i]
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        if d == 1:
            t, e, w, b = w, t, b, e
        elif d == 2:
            t, e, w, b = e, b, t, w
        elif d == 3:
            t, s, n, b = s, b, t, n
        else:
            t, s, n, b = n, t, b, s
        if arr[x][y]:
            b, arr[x][y] = arr[x][y], 0
        else:
            arr[x][y] = b
        print(t)
