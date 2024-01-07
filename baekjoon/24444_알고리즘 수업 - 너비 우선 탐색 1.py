from collections import deque
import sys


input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N)]
visit = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
for lst in graph:
    lst.sort()
cnt = 1
visit[R - 1] = cnt
q = deque([R - 1])
while q:
    u = q.popleft()
    for v in graph[u]:
        if not visit[v]:
            cnt += 1
            visit[v] = cnt
            q.append(v)
for v in visit:
    print(v)
