def bfs():
    cnt = 0
    while q_h:
        for _ in range(len(q_w)):
            r, c = q_w.pop(0)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = '*'
                        visit[nr][nc] = 1
                        q_w.append((nr, nc))
        cnt += 1
        for _ in range(len(q_h)):
            r, c = q_h.pop(0)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] == '.' and not visit[nr][nc]:
                        q_h.append((nr, nc))
                        visit[nr][nc] = 1
                    elif arr[nr][nc] == 'D':
                        return cnt
    return 'KAKTUS'


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
R, C = map(int, input().split())
arr = []
visit = [[0] * C for _ in range(R)]
q_w = []
q_h = []
for i in range(R):
    data = input()
    for j in range(C):
        if data[j] == '*':
            visit[i][j] = 1
            q_w.append((i, j))
        elif data[j] == 'X':
            visit[i][j] = 1
        elif data[j] == 'S':
            visit[i][j] = 1
            q_h.append((i, j))
    arr.append(list(data))
print(bfs())
