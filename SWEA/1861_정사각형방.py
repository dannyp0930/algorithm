import sys
sys.stdin = open('1861.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            Q = [(i, j)]
            cnt = 1
            while Q:
                r, c = Q.pop()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] - arr[r][c] == 1:
                        cnt += 1
                        Q.append((nr, nc))
            tmp[arr[i][j]] = cnt
    max_cnt = max(tmp)
    for i in range(1, N * N + 1):
        if tmp[i] == max_cnt:
            print('#{} {} {}'.format(T, i, max_cnt))
            break
