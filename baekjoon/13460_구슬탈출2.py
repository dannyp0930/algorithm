dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def move(x, y, d):
    cnt = 0
    while arr[x + dx[d]][y + dy[d]] != '#' and arr[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        cnt += 1
    return x, y, cnt


def bfs():
    while q:
        rx, ry, bx, by, cnt = q.pop(0)
        if cnt > 10:
            break
        for d in range(4):
            nrx, nry, rcnt = move(rx, ry, d)
            nbx, nby, bcnt = move(bx, by, d)
            if arr[nbx][nby] == 'O': continue
            if arr[nrx][nry] == 'O':
                return cnt
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]
            if not visit[nrx][nry][nbx][nby]:
                q.append((nrx, nry, nbx, nby, cnt + 1))
                visit[nrx][nry][nbx][nby] = 1
    return -1

N, M = map(int, input().split())
rx, ry, bx, by = 0, 0, 0, 0
arr = []
for i in range(N):
    tmp = input()
    for j in range(M):
        if tmp[j] == 'R':
            rx, ry = i, j
        elif tmp[j] == 'B':
            bx, by = i, j
    arr.append(tmp)
visit = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = [(rx, ry, bx, by, 1)]
visit[rx][ry][bx][by] = 1
print(bfs())
