# DFS/BFS
from collections import deque

N = int(input())
G = [[] for _ in range(N + 1)]
while 1:
    a, b = map(int, input().split())
    if a == -1: break
    G[a].append(b)
    G[b].append(a)
candi = []
min_score = 0xffffff
for i in range(1, N + 1):
    visit = [0] * (N + 1)
    Q = deque()
    Q.append(i)
    visit[i] = 1
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if visit[v]: continue
            visit[v] = visit[u] + 1
            Q.append(v)
        if not len(Q):
            score = visit[u] - 1
            if min_score > score:
                min_score = score
                candi = [i]
            elif min_score == score:
                candi.append(i)
print(min_score, len(candi))
print(*candi)
