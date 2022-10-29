N = int(input())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
time = [0] * (N + 1)
for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    for j in tmp[1:-1]:
        graph[j].append(i)
        in_degree[i] += 1
res = [0] * (N + 1)
q = []
for i in range(1, N + 1):
    if not in_degree[i]:
        q.append(i)
while q:
    u = q.pop(0)
    res[u] += time[u]
    for v in graph[u]:
        in_degree[v] -= 1
        res[v] = max(res[v], res[u])
        if not in_degree[v]:
            q.append(v)
for i in range(1, N + 1):
    print(res[i])
