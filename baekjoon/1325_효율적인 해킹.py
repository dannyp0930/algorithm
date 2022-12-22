import sys
from collections import deque


def bfs(i):
    visit = [0] * (N + 1)
    cnt = 1
    q = deque()
    q.append(i)
    visit[i] = 1
    while q:
        n = q.popleft()
        for v in arr[n]:
            if not visit[v]:
                cnt += 1
                q.append(v)
                visit[v] = 1
    return cnt


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[B].append(A)
max_cnt = 0
res = []
for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        res = [i]
        max_cnt = cnt
    elif cnt == max_cnt:
        res.append(i)
print(*res)
