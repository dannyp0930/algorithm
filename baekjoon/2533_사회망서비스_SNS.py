import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(n):
    visit[n] = 1
    dp[n][0] = 1
    for e in graph[n]:
        if visit[e]: continue
        dfs(e)
        dp[n][0] += min(dp[e])
        dp[n][1] += dp[e][0]


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
dp = [[0, 0] for _ in range(N + 1)]
visit = [0] * (N + 1)
dfs(1)
print(min(dp[1]))