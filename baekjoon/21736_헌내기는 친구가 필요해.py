dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = []
visit = [[0] * M for _ in range(N)]
q = []
for i in range(N):
    tmp = list(input())
    arr.append(tmp)
    for j in range(M):
        if tmp[j] == 'I':
            q.append((i, j))
            visit[i][j] = 1
ans = 0
while q:
    r, c = q.pop(0)
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] != 'X' and not visit[nr][nc]:
                visit[nr][nc] = 1
                q.append((nr, nc))
                if arr[nr][nc] == 'P':
                    ans += 1
print(ans if ans else 'TT')
