import sys
sys.stdin = open('1249.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    while Q:
        r, c = Q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                w = arr[nr][nc]
                if visit[nr][nc] > visit[r][c] + w:
                    visit[nr][nc] = visit[r][c] + w
                    Q.append((nr, nc))


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visit = [[9999999] * N for _ in range(N)]
    Q = [(0, 0)]
    visit[0][0] = 0
    bfs()
    print('#{} {}'.format(T, visit[N - 1][N - 1]))
