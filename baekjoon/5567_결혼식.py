def invite(n):
    visit[n] = 1
    for v in graph[n]:
        if not visit[v]:
            visit[v] = 1


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0] * (n + 1)
visit[1] = 1
for v in graph[1]:
    invite(v)
print(sum(visit) - 1)
