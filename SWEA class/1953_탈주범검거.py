import sys
sys.stdin = open('1953.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def boundary(a, b):
    return 0 <= a < N and 0 <= b < M and not visit[a][b]


def up(n, a, b):
    return n == 0 and arr[a][b] in (1, 2, 5, 6)


def down(n, a, b):
    return n == 1 and arr[a][b] in (1, 2, 4, 7)


def left(n, a, b):
    return n == 2 and arr[a][b] in (1, 3, 4, 5)


def right(n, a, b):
    return n == 3 and arr[a][b] in (1, 3, 6, 7)


def escape():
    while Q:
        r, c = Q.pop(0)
        if arr[r][c] == 1:
            lst = [0, 1, 2, 3]
        elif arr[r][c] == 2:
            lst = [0, 1]
        elif arr[r][c] == 3:
            lst = [2, 3]
        elif arr[r][c] == 4:
            lst = [0, 3]
        elif arr[r][c] == 5:
            lst = [1, 3]
        elif arr[r][c] == 6:
            lst = [1, 2]
        else:
            lst = [0, 2]
        for k in lst:
            nr, nc = r + dr[k], c + dc[k]
            if boundary(nr, nc):
                if up(k, nr, nc) or down(k, nr, nc) or left(k, nr, nc) or right(k, nr, nc):
                    Q.append((nr, nc))
                    visit[nr][nc] = visit[r][c] + 1


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    visit[R][C] = 1
    Q = [(R, C)]
    escape()
    result = 0
    for i in range(N):
        for j in range(M):
            if 0 < visit[i][j] <= L:
                result += 1
    print('#{} {}'.format(tc, result))
