import sys
from collections import deque


def bfs(F, S, G, U, D):
    visit = [-1] * (F + 1)
    q = deque([S])
    visit[S] = 0
    while q:
        now = q.popleft()
        if now == G:
            return visit[G]
        for i in (U, -D):
            new = now + i
            if new < 1 or new > F:
                continue
            if visit[new] == -1:
                q.append(new)
                visit[new] = visit[now] + 1
    return 'use the stairs'


input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
print(bfs(F, S, G, U, D))