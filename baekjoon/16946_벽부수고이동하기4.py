from collections import deque
import sys
input = sys.stdin.readline


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def boundary(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    res = 1
    while q:
        r, c = q.popleft()
        zero[r][c] = zero_cnt
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not boundary(nr, nc): continue
            if visit[nr][nc]: continue
            if arr[nr][nc]: continue
            q.append((nr, nc))
            visit[nr][nc] = 1
            res += 1
    return res

def countMoves(r, c):
    candi = set()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not boundary(nr, nc): continue
        if not zero[nr][nc]: continue
        candi.add(zero[nr][nc])
    tmp = 1
    for cnt in candi:
        tmp += zero_dict[cnt]
        tmp %= 10
    return tmp 

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]
zero = [[0] * M for _ in range(N)]
zero_cnt = 1
zero_dict = {}
for r in range(N):
    for c in range(M):
        if not arr[r][c] and not visit[r][c]:
            zero_dict[zero_cnt] = bfs(r, c)
            zero_cnt += 1
for r in range(N):
    for c in range(M):
        if arr[r][c]:
            ans[r][c] = countMoves(r, c)
for lst in ans:
    for i in range(M):
        print(lst[i], end="")
    print()