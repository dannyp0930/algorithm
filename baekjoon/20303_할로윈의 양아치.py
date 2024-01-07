from collections import deque
import sys
input = sys.stdin.readline


def bfs(x):
    q = deque([x])
    group = [x]
    cnt = candies[x]
    visit[x] = 1
    while q:
        n = q.popleft()
        for v in friends[n]:
            if not visit[v]:
                q.append(v)
                group.append(v)
                cnt += candies[v]
                visit[v] = 1
    return group, cnt


N, M, K = map(int, input().split())
candies = list(map(int, input().split()))
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)
visit = [0] * N
groups = []
for i in range(N):
    if not visit[i]:
        groups.append(bfs(i))
dp = [[0] * (K + 1) for _ in range(len(groups))]
for i, group in enumerate(groups):
    children, candy = len(group[0]), group[1]
    for k in range(1, K + 1):
        if k <= children:
            dp[i][k] = dp[i - 1][k]
        else:
            dp[i][k] = max(dp[i - 1][k - children] + candy, dp[i - 1][k])
print(dp[-1][K])
