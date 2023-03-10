dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visit = [[0] * C for _ in range(R)]
s = w = 0
for i in range(R):
    for j in range(C):
        if not visit[i][j] and arr[i][j] != '#':
            q = [(i, j)]
            visit[i][j] = 1
            cnt_o = cnt_v = 0
            if arr[i][j] == 'o':
                cnt_o += 1
            elif arr[i][j] == 'v':
                cnt_v += 1
            while q:
                r, c = q.pop(0)

                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and not visit[nr][nc]:
                        if arr[nr][nc] == '#':
                            continue
                        elif arr[nr][nc] == 'o':
                            cnt_o += 1
                        elif arr[nr][nc] == 'v':
                            cnt_v += 1
                        q.append((nr, nc))
                        visit[nr][nc] = 1
            if cnt_o > cnt_v:
                s += cnt_o
            else:
                w += cnt_v
print(s, w)
