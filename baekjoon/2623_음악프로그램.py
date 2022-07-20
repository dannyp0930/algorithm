N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1, len(order) - 1):
        graph[order[i]].append(order[i + 1])
        in_degree[order[i + 1]] += 1
q = []
for i in range(1, N + 1):
    if not in_degree[i]:
        q.append(i)
res = []
while q:
    u = q.pop(0)
    res.append(u)
    for v in graph[u]:
        in_degree[v] -= 1
        if not in_degree[v]:
            q.append(v)
if len(res) != N:
    print(0)
else:
    for n in res:
        print(n)
