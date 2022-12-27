def bfs(i, j, color):
    q = [(i, j)]
    cnt = 1
    tmp = [(i, j)]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 12 and 0 <= nc < 6:
                if not visit[nr][nc] and arr[nr][nc] == color:
                    cnt += 1
                    visit[nr][nc] = 1
                    q.append((nr, nc))
                    tmp.append((nr, nc))
    if cnt > 3:
        for r, c in tmp:
            arr[r][c] = '.'
        return True
    return False


def fall():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if arr[j][i] != '.' and arr[k][i] == '.':
                    arr[k][i], arr[j][i] = arr[j][i], '.'
                    break


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
arr = [list(input()) for _ in range(12)]
ans = 0
while 1:
    flag = False
    visit = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if not visit[i][j] and arr[i][j] != '.':
                visit[i][j] = 1
                tmp = bfs(i, j, arr[i][j])
                if tmp:
                    flag = True
    if not flag:
        break
    ans += 1
    fall()
print(ans)
