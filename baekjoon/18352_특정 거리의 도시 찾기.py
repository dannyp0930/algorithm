import sys
from collections import deque


def bfs(s):
    ans = []
    q = deque([(s, 0)])
    visit = [0] * (N + 1)
    visit[s] = 1
    while q:
        n, t = q.popleft()
        if t == K:
            ans.append(n)
        for v in graph[n]:
            if not visit[v]:
                visit[v] = 1
                q.append((v, t + 1))
    if not ans:
        print(-1)
    else:
        ans.sort()
        for n in ans:
            print(n)


input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
bfs(X)
