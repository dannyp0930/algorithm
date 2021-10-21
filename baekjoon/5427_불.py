# DFS/BFS

from collections import deque


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def boundary(x, y):
    return 0 <= x < h and 0 <= y < w


def bfs():
    global Q, fire
    while Q:
        tmp1 = deque()
        while Q:
            r, c = Q.popleft()
            if r == 0 or c == 0 or r == h - 1 or c == w - 1:
                if arr[r][c] != '*':
                    return arr[r][c] + 1
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if not boundary(nr, nc): continue
                if arr[nr][nc] == '.' and arr[r][c] != '*':
                    arr[nr][nc] = arr[r][c] + 1
                    tmp1.append((nr, nc))
        Q = tmp1
        tmp2 = deque()
        while fire:
            fr, fc = fire.popleft()
            for k in range(4):
                nfr, nfc = fr + dr[k], fc + dc[k]
                if not boundary(nfr, nfc): continue
                if not visit[nfr][nfc] and arr[nfr][nfc] != '#':
                    arr[nfr][nfc] = '*'
                    visit[nfr][nfc] = 1
                    tmp2.append((nfr, nfc))
        fire = tmp2
    return 'IMPOSSIBLE'


for T in range(int(input())):
    w, h = map(int, input().split())
    time_limit = w * h
    arr = []
    visit = [[0] * w for _ in range(h)]
    Q = deque()
    fire = deque()
    for i in range(h):
        lst = list(map(str, input()))
        for j in range(w):
            if lst[j] == '@':
                Q.append((i, j))
                lst[j] = 0
                visit[i][j] = 1
            if lst[j] == '*':
                fire.append((i, j))
        arr.append(lst)
    print(bfs())
