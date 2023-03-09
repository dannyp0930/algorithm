import sys
input = sys.stdin.readline


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def rotate(i, j, R, C):
    d = 0
    r, c = i, j
    tmp = A[r][c]
    while 1:
        if d == 4:
            break
        nr, nc = r + dr[d], c + dc[d]
        if i <= nr < R + i and j <= nc < C + j:
            A[nr][nc], tmp = tmp, A[nr][nc]
            r, c = nr, nc
        else:
            d += 1


N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    i, j, R, C = 0, 0, N, M
    while 1:
        rotate(i, j, R, C)
        i += 1
        j += 1
        R -= 2
        C -= 2
        if R < 2 or C < 2:
            break
for lst in A:
    print(*lst)
