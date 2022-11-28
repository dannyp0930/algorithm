import sys

input = sys.stdin.readline
N, K = map(int, input().split())
visit = [0] * 100001
queue = [N]
visit[N] = 1
while queue:
    x = queue.pop(0)
    if x == K:
        break
    x1, x2, x3 = x * 2, x - 1, x + 1
    if 0 <= x1 <= 100000 and not visit[x1]:
        visit[x1] = visit[x]
        queue.append(x1)
    if 0 <= x2 <= 100000 and not visit[x2]:
        visit[x2] = visit[x] + 1
        queue.append(x2)
    if 0 <= x3 <= 100000 and not visit[x3]:
        visit[x3] = visit[x] + 1
        queue.append(x3)
print(visit[K] - 1)