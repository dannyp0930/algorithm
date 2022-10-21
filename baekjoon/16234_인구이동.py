import sys


def bfs(i, j):
    q = [(i, j)]
    res = [(i, j)]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visit[nr][nc]:
                continue
            if L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                visit[nr][nc] = True
                q.append((nr, nc))
                res.append((nr, nc))
    return res


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while 1:
    visit = [[False] * N for _ in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j] = True
                union = bfs(i, j)
                cnt = len(union)
                if cnt > 1:
                    move = True
                    pop = sum([arr[r][c] for r, c in union]) // cnt
                    for r, c in union:
                        arr[r][c] = pop
    if not move:
        break
    ans += 1
print(ans)
