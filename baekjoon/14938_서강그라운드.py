INF = 0xfffffff
n, m, r = map(int, input().split())
t = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))
max_items = 0
for i in range(n):
    dist = [INF] * n
    visit = [0] * n
    s = i
    dist[s] = 0
    for _ in range(n):
        visit[s] = 1
        for e, l in graph[s]:
            dist[e] = min(dist[e], dist[s] + l)
        min_value = INF
        for j in range(n):
            if not visit[j] and min_value > dist[j]:
                s, min_value = j, dist[j]
    sum_items = 0
    for k in range(n):
        if dist[k] <= m:
            sum_items += t[k]
    max_items = max(max_items, sum_items)
print(max_items)