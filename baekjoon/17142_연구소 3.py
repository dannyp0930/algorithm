import sys
from itertools import combinations
from collections import deque


input = sys.stdin.readline
INF = float('inf')
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
virus = []
arr = []
empty = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 0:
            empty += 1
        elif tmp[j] == 2:
            virus.append((i, j))
    arr.append(tmp)
ans = INF
for candi in combinations(virus, M):
    cnt = 0
    time = 0
    graph = []
    for lst in arr:
        graph.append(lst[:])
    q = deque()
    visit = [[-1] * N for _ in range(N)]
    for i, j in candi:
        q.append((i, j, 0))
        visit[i][j] = 0
    while q:
        r, c, t = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if graph[nr][nc] != 1 and visit[nr][nc] == -1:
                visit[nr][nc] = t + 1
                q.append((nr, nc, t + 1))
                if graph[nr][nc] == 0:
                    time = max(time, t + 1)
                    cnt += 1
    if cnt == empty:
        ans = min(ans, time)
if ans == INF:
    ans = -1
print(ans)
