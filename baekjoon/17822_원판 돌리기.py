import sys
from collections import deque


def bfs(i, j):
    global flag
    q = deque([(i, j)])
    num = arr[i][j]
    tmp = [(i, j)]
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nc < 0:
                nc = M - 1
            elif nc >= M:
                nc = 0
            if 0 <= nr < N and not visit[nr][nc] and arr[nr][nc] == num:
                visit[nr][nc] = 1
                q.append((nr, nc))
                tmp.append((nr, nc))
    if len(tmp) > 1:
        for x, y in tmp:
            arr[x][y] = 0
        flag = True


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
input = sys.stdin.readline
N, M, T = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    x, d, k = map(int, input().split())
    d = 1 if d == 0 else -1
    for i in range(1, N // x + 1):
        idx = x * i - 1
        arr[idx].rotate(d * k)
    flag = False
    visit = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c] != 0 and not visit[r][c]:
                visit[r][c] = 1
                bfs(r, c)
    if not flag:
        tot = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]:
                    tot += arr[i][j]
                    cnt += 1
        if not cnt:
            break
        mean = tot / cnt
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    continue
                elif arr[i][j] < mean:
                    arr[i][j] += 1
                elif arr[i][j] > mean:
                    arr[i][j] -= 1
ans = 0
for dq in arr:
    ans += sum(dq)
print(ans)
