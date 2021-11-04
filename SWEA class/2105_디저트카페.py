import sys
sys.stdin = open('2105.txt', 'r')

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def tour(x, y, a, b):
    global ans
    r, c = x, y
    tmp = []
    for k in range(4):
        cnt = a if not k % 2 else b
        for _ in range(cnt):
            nr, nc = r + dr[k], c + dc[k]
            if not (0 <= nr < N and 0 <= nc < N) or arr[nr][nc] in tmp:
                return
            r, c = nr, nc
            tmp.append(arr[r][c])
    if ans < len(tmp):
        ans = len(tmp)


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            for m in range(1, N - 1):
                for n in range(1, N - 1):
                    tour(i, j, m, n)
    print('#{} {}'.format(T, ans))
